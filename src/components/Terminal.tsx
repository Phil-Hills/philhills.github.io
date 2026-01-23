import React, { useState, useEffect, useRef } from 'react';
import { useTerminal } from '../hooks/useTerminal';
import { ZCurveViz } from './ZCurveViz';

export const Terminal: React.FC = () => {
    const { history, cwd, execute } = useTerminal();
    const [inputVal, setInputVal] = useState('');
    const inputRef = useRef<HTMLInputElement>(null);
    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        if (bottomRef.current) {
            bottomRef.current.scrollIntoView({ behavior: 'auto' });
        }
    }, [history]);

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') {
            execute(inputVal);
            setInputVal('');
        }
    };

    const focusInput = () => {
        inputRef.current?.focus();
    };

    return (
        <div
            className="min-h-screen bg-terminal-bg text-terminal-text font-mono p-4 sm:p-6 overflow-hidden flex flex-col"
            onClick={focusInput}
        >
            <div className="max-w-4xl mx-auto w-full flex-grow flex flex-col">
                {history.map((item, i) => (
                    <div key={i} className="mb-1 leading-relaxed break-words">
                        {item.type === 'input' ? (
                            <div className="flex">
                                <span className="text-terminal-accent mr-3 select-none">
                                    phil@node-sea:{item.cwd}$
                                </span>
                                <span>{item.content}</span>
                            </div>
                        ) : item.type === 'component' ? (
                            <div className="my-2">
                                <div className="text-terminal-text opacity-90 mb-1">{item.content}</div>
                                {item.componentName === 'ZCurveViz' && (
                                    <ZCurveViz count={item.componentProps?.count || 50} />
                                )}
                            </div>
                        ) : item.type === 'error' ? (
                            <div className="text-red-500 whitespace-pre-wrap">{item.content}</div>
                        ) : (
                            <div className="text-terminal-text whitespace-pre-wrap opacity-90">
                                {item.content}
                            </div>
                        )}
                    </div>
                ))}

                <div className="flex mt-2">
                    <span className="text-terminal-accent mr-3 select-none">
                        phil@node-sea:{cwd}$
                    </span>
                    <input
                        ref={inputRef}
                        type="text"
                        value={inputVal}
                        onChange={(e) => setInputVal(e.target.value)}
                        onKeyDown={handleKeyDown}
                        className="bg-transparent border-none outline-none flex-grow text-terminal-text caret-terminal-accent"
                        autoFocus
                        autoComplete="off"
                        spellCheck="false"
                    />
                </div>
                <div ref={bottomRef} />
            </div>
        </div>
    );
};
