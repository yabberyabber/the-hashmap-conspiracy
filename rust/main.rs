extern crate rand;

use std::collections::HashMap;
use rand::Rng;
use std::env;

fn main() {
    if let Some(arg1) = env::args().nth(1) {
        let mut subject: HashMap<u64, u64> = HashMap::new();
        let mut rng = rand::thread_rng();

        let size = arg1.parse::<u64>().unwrap();

        for i in 0u64..size {
            subject.insert(i + (size * (rng.gen::<u64>() % size)), i);
        }
    }
}
