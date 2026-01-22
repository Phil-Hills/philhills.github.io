/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                terminal: {
                    bg: '#050505',
                    text: '#e0e0e0',
                    accent: '#00ff9d',
                    dim: '#666666',
                    border: '#333333',
                }
            },
            fontFamily: {
                mono: ['"Courier New"', 'Courier', 'monospace'],
                sans: ['Inter', 'sans-serif'],
            },
            animation: {
                'blink': 'blink 1s step-end infinite',
            },
            keyframes: {
                blink: {
                    '0%, 100%': { opacity: '1' },
                    '50%': { opacity: '0' },
                }
            }
        },
    },
    plugins: [],
}
