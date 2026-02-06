import React, { useRef, useState } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Text, OrbitControls, useCursor } from '@react-three/drei';
import * as THREE from 'three';

function Voxel({ ...props }) {
    const mesh = useRef<THREE.Mesh>(null!);
    const [hovered, setHover] = useState(false);
    const [active, setActive] = useState(false);

    useCursor(hovered);

    useFrame((_, delta) => {
        if (!active) {
            mesh.current.rotation.x += delta * 0.2;
            mesh.current.rotation.y += delta * 0.2;
        }
    });

    return (
        <mesh
            {...props}
            ref={mesh}
            scale={active ? 1.5 : 1}
            onClick={() => setActive(!active)}
            onPointerOver={() => setHover(true)}
            onPointerOut={() => setHover(false)}
        >
            <boxGeometry args={[2.5, 2.5, 2.5]} />
            <meshStandardMaterial color={hovered ? '#00ff9d' : '#111111'} wireframe={true} />

            {/* Front Face - Identity */}
            <Text position={[0, 0, 1.3]} fontSize={0.2} color="#00ff9d" anchorX="center" anchorY="middle">
                PHIL HILLS
            </Text>
            <Text position={[0, -0.3, 1.3]} fontSize={0.1} color="#ffffff" anchorX="center" anchorY="middle">
                0x923-SEA
            </Text>

            {/* Back Face - Protocol */}
            <Text position={[0, 0, -1.3]} rotation={[0, Math.PI, 0]} fontSize={0.2} color="#00ff9d" anchorX="center" anchorY="middle">
                Q PROTOCOL
            </Text>
            <Text position={[0, -0.3, -1.3]} rotation={[0, Math.PI, 0]} fontSize={0.1} color="#ffffff" anchorX="center" anchorY="middle">
                V1.2 ACTIVE
            </Text>

            {/* Right Face - Verification */}
            <Text position={[1.3, 0, 0]} rotation={[0, Math.PI / 2, 0]} fontSize={0.15} color="#00ff9d" anchorX="center" anchorY="middle">
                VERIFIED
            </Text>
            <Text position={[1.3, -0.3, 0]} rotation={[0, Math.PI / 2, 0]} fontSize={0.1} color="#ffffff" anchorX="center" anchorY="middle">
                SIG: 4F8A...
            </Text>

            {/* Left Face - Status */}
            <Text position={[-1.3, 0, 0]} rotation={[0, -Math.PI / 2, 0]} fontSize={0.15} color="#00ff9d" anchorX="center" anchorY="middle">
                STATUS
            </Text>
            <Text position={[-1.3, -0.3, 0]} rotation={[0, -Math.PI / 2, 0]} fontSize={0.1} color="#ffffff" anchorX="center" anchorY="middle">
                COMPLIANT
            </Text>

        </mesh>
    );
}

export const AgentVoxel: React.FC = () => {
    return (
        <div className="mt-4 border border-terminal-border bg-terminal-bg rounded shadow-lg animate-fade-in w-full h-[400px]">
            <h3 className="text-terminal-accent font-mono text-sm px-4 py-2 border-b border-terminal-border flex justify-between">
                <span>AGENT VOXEL [Identity Node]</span>
                <span className="text-terminal-dim">Interactive (Click to Inspect)</span>
            </h3>
            <Canvas className="w-full h-full bg-[#050505]">
                <ambientLight intensity={0.5} />
                <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} />
                <pointLight position={[-10, -10, -10]} />
                <Voxel position={[0, 0, 0]} />
                <OrbitControls enableZoom={false} />
                <gridHelper args={[10, 10, 0x333333, 0x111111]} position={[0, -2, 0]} />
            </Canvas>
        </div>
    );
};
