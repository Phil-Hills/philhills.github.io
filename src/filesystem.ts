export type FileSystemNode = string | { [key: string]: FileSystemNode };

export const fileSystem: { [key: string]: FileSystemNode } = {
    "~": {
        "projects": {
            "q-protocol.md": `# Q Protocol
      
The standard for Z-Order Telemetry in Agentic Systems.

- **Status**: Production (V1.2)
- **Compression**: 40x vs JSON
- **Latency**: <50ms Mesh Propagation

Run 'spawn --count 50' to visualize mesh latency.`,

            "agent-voxel.md": `# Agent Voxels
      
Atomic units of semantic memory for agents.
Ensures context retention without token bloat. (Formerly Identity Cube)`,
        },
        "bio.txt": `PHIL HILLS
Systems Architect | Seattle, WA

Architeching the "Agentic Internet".
Creator of Q Protocol.
`,
        "contact.txt": `Email: phil@philhills.com
GitHub: github.com/Phil-Hills
LinkedIn: linkedin.com/in/philhills
`
    }
};
