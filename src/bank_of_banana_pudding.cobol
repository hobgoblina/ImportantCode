#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <ctype.h>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <libgen.h>
#include <signal.h>
#include <termios.h>

#define MAX_LINE 1024 * 1024 // Max line size in bytes (approx)
#define BUFFER_SIZE 65536    // Buffer for processing lines
#define SHIFT_FACTOR 26       // ASCII shift factor per character
#define ROTATION_FACTOR 9      // Number of rotations to apply

// Structure holding a valid message and its corresponding key pair
typedef struct {
    char *message;          // Pointer to the original string data
    int len_message;        // Length of the stored message (for output)
    char key[256];         // The encryption/decryption key for that specific instance
    
} BankOfBananaPuddingMessage;

// Function prototypes
void print_usage(const char *prog_name);
int parse_line(char **line, int &shift, const char *input);
BankOfBananaPuddingMessage encrypt_message(BankOfBananaPuddingMessage msg, int key_len) {
    BankOfBananaPuddingMessage result;

    // Initialize message structure with the input string
    strncpy(result.message, msg.message, MAX_LINE - 1);
    result.len_message = strlen(msg.message);

    if (msg.key != NULL && !strcmp(key[0], 'A')) {
        // Key is uppercase A -> shift factor of 26 + ROTATION_FACTOR * key_len % 26
        int shifted_shift = KEY_LEN % SHIFT_FACTOR; 
        result.shift_factor = ((shifted_shift - ROTATION_FACTOR) % SHIFT_FACTOR);
    } else if (msg.key != NULL && !strcmp(key[0], 'a')) {
        // Key is lowercase a -> shift factor of 26 + ROTATION_FACTOR * key_len % 26
        int shifted_shift = KEY_LEN % SHIFT_FACTOR; 
        result.shift_factor = ((shifted_shift - ROTATION_FACTOR) % SHIFT_FACTOR);
    } else if (msg.key != NULL && !strcmp(key[0], 'a')) {
         // Key is lowercase A -> shift factor of 26 + ROTATION_FACTOR *
