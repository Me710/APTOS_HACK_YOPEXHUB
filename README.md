# Rust WebAssembly Project with Yew and Aptos Integration

This project is a web application built using Rust, WebAssembly, and the Yew framework, with integration for the Aptos blockchain.

## Prerequisites

1. **Rust**: Install the latest stable version from [rustup.rs](https://rustup.rs/)
2. **Cargo**: Comes with Rust. Verify with `cargo --version`
3. **wasm-bindgen-cli**: Install using `cargo install wasm-bindgen-cli`
4. **Node.js and npm**: Download from [nodejs.org](https://nodejs.org/)
5. **Aptos CLI**: Follow installation instructions from [Aptos CLI documentation](https://aptos.dev/cli-tools/aptos-cli-tool/install-aptos-cli)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/Me710/APTOS_HACK_YOPEXHUB.git
   cd APTOS_HACK_YOPEXHUB
   ```

2. Add the WebAssembly target:
   ```
   rustup target add wasm32-unknown-unknown
   ```

3. Install Aptos SDK:
   Add the following to your `Cargo.toml`:
   ```toml
   [dependencies]
   aptos-sdk = { git = "https://github.com/aptos-labs/aptos-core.git", rev = "devnet" }
   ```

4. Set up an Aptos account:
   ```
   aptos init
   ```
   Follow the prompts to create a new account or import an existing one.

## Building the Project

1. Build for WebAssembly:
   ```
   cargo build --target wasm32-unknown-unknown
   ```

2. Generate JavaScript bindings:
   ```
   wasm-bindgen --target web --out-dir ./pkg ./target/wasm32-unknown-unknown/debug/code_rust.wasm
   ```

## Running the Project

1. Start a local server:
   ```
   npx http-server
   ```

2. Open `http://localhost:8080` in your browser.


## Project Structure

- `src/lib.rs`: Main application logic and Aptos interactions
- `src/main.rs`: Entry point for native binary (not used in web context)
- `Cargo.toml`: Rust dependencies including Aptos SDK
- `index.html`: HTML file to load the WebAssembly module

## Development Workflow

1. Modify Rust code in `src/`.
2. Rebuild and regenerate bindings.
3. Test Aptos interactions carefully, preferably on testnet first.
4. Refresh browser to see changes.

## Troubleshooting

- For Aptos-specific issues, check the [Aptos documentation](https://aptos.dev/).
- Ensure your Aptos account has sufficient funds for transactions.
- Verify network settings (mainnet, testnet, devnet) in your Aptos configurations.

## Security Considerations

- Never expose private keys in client-side code.
- Use secure methods for handling sensitive information.
- Consider implementing a backend service for sensitive operations.
