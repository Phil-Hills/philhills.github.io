import { useState, useCallback, useEffect } from 'react';
import { fileSystem, FileSystemNode } from '../filesystem';

type HistoryItem = {
    type: 'input' | 'output' | 'error';
    content: string;
    cwd?: string;
};

export const useTerminal = () => {
    const [history, setHistory] = useState<HistoryItem[]>([
        { type: 'output', content: 'Q Protocol Kernel [Version 1.2.0]' },
        { type: 'output', content: '(c) 2026 Q Protocol Research. All rights reserved.\n' },
        { type: 'output', content: 'Connection established: node-sea-01' },
        { type: 'output', content: 'Type "help" for available commands.\n' },
    ]);
    const [cwd, setCwd] = useState<string[]>(['~']);

    const addToHistory = (item: HistoryItem) => {
        setHistory(prev => [...prev, item]);
    };

    const resolvePath = (path: string[]): FileSystemNode | null => {
        let current: FileSystemNode = fileSystem;
        for (const part of path) {
            if (typeof current === 'string') return null;
            if (current[part] === undefined) return null;
            current = current[part];
        }
        return current;
    };

    const execute = useCallback((commandStr: string) => {
        const trimmed = commandStr.trim();
        if (!trimmed) {
            addToHistory({ type: 'input', content: '', cwd: cwd.join('/') });
            return;
        }

        addToHistory({ type: 'input', content: trimmed, cwd: cwd.join('/') });

        const parts = trimmed.split(' ');
        const cmd = parts[0].toLowerCase();
        const args = parts.slice(1);

        switch (cmd) {
            case 'help':
                addToHistory({
                    type: 'output',
                    content: `Available commands:
  ls        List directory contents
  cd <dir>  Change directory
  cat <file> Display file contents
  clear     Clear terminal screen
  help      Show this help message
  
Special commands:
  spawn     Visualize Q Protocol agents (Coming in Phase 3)
`
                });
                break;

            case 'clear':
                setHistory([]);
                break;

            case 'ls':
                const node = resolvePath(cwd);
                if (typeof node === 'object') {
                    const contents = Object.keys(node).map(key => {
                        const isDir = typeof node[key] !== 'string';
                        return isDir ? `${key}/` : key;
                    }).join('  ');
                    addToHistory({ type: 'output', content: contents });
                } else {
                    addToHistory({ type: 'error', content: 'Not a directory' });
                }
                break;

            case 'cat':
                if (args.length === 0) {
                    addToHistory({ type: 'error', content: 'Usage: cat <filename>' });
                    break;
                }
                const target = args[0];
                const fileNode = resolvePath([...cwd, target]);

                if (typeof fileNode === 'string') {
                    addToHistory({ type: 'output', content: fileNode });
                } else if (fileNode === null) {
                    addToHistory({ type: 'error', content: `File not found: ${target}` });
                } else {
                    addToHistory({ type: 'error', content: `${target} is a directory` });
                }
                break;

            case 'cd':
                if (args.length === 0) {
                    setCwd(['~']);
                    break;
                }
                if (args[0] === '..') {
                    if (cwd.length > 1) setCwd(prev => prev.slice(0, -1));
                } else {
                    const targetDir = args[0].replace(/\/$/, '');
                    const newPath = [...cwd, targetDir];
                    const targetNode = resolvePath(newPath);
                    if (targetNode && typeof targetNode !== 'string') {
                        setCwd(newPath);
                    } else {
                        addToHistory({ type: 'error', content: `Directory not found: ${targetDir}` });
                    }
                }
                break;

            default:
                addToHistory({ type: 'error', content: `Command not found: ${cmd}` });
        }
    }, [cwd]);

    return {
        history,
        cwd: cwd.join('/'),
        execute
    };
};
