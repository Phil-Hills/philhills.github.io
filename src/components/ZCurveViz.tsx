import React, { useEffect, useRef, useState } from 'react';

interface ZCurveVizProps {
    count: number;
}

// Interleave bits of two 16-bit integers
function mortonEncode(x: number, y: number): number {
    x &= 0xFFFF;
    x = (x | (x << 8)) & 0x00FF00FF;
    x = (x | (x << 4)) & 0x0F0F0F0F;
    x = (x | (x << 2)) & 0x33333333;
    x = (x | (x << 1)) & 0x55555555;

    y &= 0xFFFF;
    y = (y | (y << 8)) & 0x00FF00FF;
    y = (y | (y << 4)) & 0x0F0F0F0F;
    y = (y | (y << 2)) & 0x33333333;
    y = (y | (y << 1)) & 0x55555555;

    return x | (y << 1);
}

export const ZCurveViz: React.FC<ZCurveVizProps> = ({ count }) => {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    const [metrics, setMetrics] = useState({ jsonSize: 0, qSize: 0, reduction: 0 });

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        // Generate random agent positions
        const width = canvas.width;
        const height = canvas.height;
        const points: { x: number, y: number, z: number, id: number }[] = [];
        const rawData = [];

        // Clear
        ctx.fillStyle = '#111';
        ctx.fillRect(0, 0, width, height);

        for (let i = 0; i < count; i++) {
            const x = Math.floor(Math.random() * width);
            const y = Math.floor(Math.random() * height);
            // Normalize 0-255 for Morton encoding
            const qx = Math.floor((x / width) * 255);
            const qy = Math.floor((y / height) * 255);

            const z = mortonEncode(qx, qy);
            points.push({ x, y, z, id: i });

            rawData.push({ id: i, pos: { x, y }, status: 'active' });
        }

        // Sort by Z-Order
        points.sort((a, b) => a.z - b.z);

        // Draw path
        ctx.beginPath();
        ctx.strokeStyle = '#00ff9d';
        ctx.lineWidth = 1;
        ctx.globalAlpha = 0.5;

        points.forEach((p, index) => {
            if (index === 0) ctx.moveTo(p.x, p.y);
            else ctx.lineTo(p.x, p.y);
        });
        ctx.stroke();

        // Draw points (Agents)
        ctx.globalAlpha = 1.0;
        points.forEach(p => {
            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
            ctx.fill();
        });

        // Calculate metrics
        const jsonBytes = JSON.stringify(rawData).length;
        const qBytes = count * 4; // 32-bit int per agent

        setMetrics({
            jsonSize: jsonBytes,
            qSize: qBytes,
            reduction: Math.round((1 - (qBytes / jsonBytes)) * 100)
        });

    }, [count]);

    return (
        <div className="mt-4 border border-terminal-border bg-terminal-bg p-4 rounded shadow-lg animate-fade-in">
            <h3 className="text-terminal-accent font-mono text-sm mb-2 border-b border-terminal-border pb-1">
                Q PROTOCOL VISUALIZER [Z-Order Mesh]
            </h3>
            <div className="flex gap-4 mb-4 font-mono text-xs">
                <div><span className="text-terminal-dim">Agents:</span> {count}</div>
                <div><span className="text-terminal-dim">Latency:</span> {(count * 0.05).toFixed(2)}ms</div>
            </div>

            <canvas ref={canvasRef} width={600} height={300} className="w-full h-[300px] bg-[#111] rounded border border-terminal-border/50" />

            <div className="flex justify-between mt-4 font-mono text-xs border-t border-terminal-border pt-2 text-terminal-dim">
                <div className="text-red-400">JSON Payload: {(metrics.jsonSize / 1024).toFixed(2)} KB</div>
                <div className="text-terminal-accent font-bold">Q Protocol: {(metrics.qSize / 1024).toFixed(2)} KB (-{metrics.reduction}%)</div>
            </div>
        </div>
    );
};
