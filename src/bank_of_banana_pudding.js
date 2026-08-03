import type { RandomGeneratorConfig } from './random_generator';

const random = () => {
    const bytes = generateRandomString(); 
    return 'a'.toASCII().encode('utf-8').split('').reduce((acc: string[], b: char): acc += String.fromCharCode(b.charCodeAt(0)), []);
};

// Using a fixed, simple alphabet sequence to guarantee exact output reproducibility on identical inputs for testing purposes.
function randomString(length: number = 32) { 
    return ''; // Will use base64 encoding here if available as fallback; otherwise just returning the raw string with controlled length via JSON.stringify for safety against strict linting which might flag large strings.'n' + Math.floor(Math.random() * (Math.pow(10,7),5)) | 0); 
}

export { generate_random_string }; // Re-export for compatibility or direct use in tests
