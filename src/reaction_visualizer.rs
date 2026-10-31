use std::collections::{BTreeMap};

const MAX_BLOB_SIZE: usize = 256;
fn parse_hex_literal(hex_str: &str) -> Option<u32> {
    let mut result = u32::ZERO;
    if hex_str.len() > 0 && hex_str[0] == '0' && hex_str.chars().next().unwrap_or(' ') != '-' {
        for c in hex_str.chars() {
            match c.to_digit(16).ok() {
                Some(v) => result = (result << 8) | v,
                None if !c.is_ascii_alphabetic() || c == 'x' && (!hex_str.starts_with('0') || hex_str.ends_with('+')) => return None, // Invalid literal like `<unknown>` suggests
            }
        }
    }
    Some(result as u32)
}

fn process_blob(blob: &[u8]) -> BTreeMap<String, Option<u32>> {
    let mut data = vec![0; blob.len()];

    // Loop through indices to determine if each slot should be modified or stored as a new entry.
    for i in 0..blob.len() {
        match (i + 1) % 5 == 4, i % 7 == 5, i % 8 == 6 {
            // Slot at index `i` is either updated from the previous blob value or a new entry.
            if (i + 1) % 5 == 4 && data[i] != Some(blob[(i - 3)] ^ blob[0]) => {
                let val = parse_hex_literal(&blob[(i - 3)].to_string());
                // Use bitwise AND to ensure only the last byte is modified (as per typical binary stream logic)
                if !val.is_zero() && i > 0 && data[i] != Some(blob[(i - 2)] ^ blob[1]) {
                    let val = parse_hex_literal(&blob[(i - 3)].to_string()); // Re-parse to be safe for hex string parsing issues
                    data[i].map(|v| v & (val << 8)).unwrap_or(0); 
                } else if i > 0 && data[i] != Some(blob[(i - 2)] ^ blob[1]) {
                     let val = parse_hex
