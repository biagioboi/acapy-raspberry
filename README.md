# Hypeledger Aries for RaspberryPI

Aries offers a stable and secure communication channel between two agents. In this project I want to create a Verifiable Credentials (VCs) using JSON-LD formatted credentials for creating a strong authentication for Web of Things-compliant devices.
In the example I will use the RaspberryPI as a possible node device interested in verifying his identity using VC.

## Setup

As prerequisite is necessary to install `Python3` for the execution of agent and script and `Cargo` for compiling the libraries, in my case I used the version 3.9.2 for Python and 1.72.0 for Cargo.

Cargo is needed since the current version of Aries Cloud Agent (ACA)-Py does not offer direct support for Raspberry architecture. It is needed to download and compile the following libraries:
```bash
git clone https://github.com/hyperledger/indy-shared-rs
cd indy-shared-rs && git checkout v1.0.3
cargo build --release
cp target/release/libindy_credx.so /wrappers/python/indy-credx/libindy_credx.so
pip3.9 install -e ~/indy-shared-rs/wrappers/python
cd ..
```
```bash
git clone https://github.com/hyperledger/indy-vdr
cd indy-vdr && git checkout v0.4.0
cargo build --release
cp target/release/libindy_vdr.so /wrappers/python/indy_vdr/libindy_vdr.so
pip3.9 install -e ~/indy-vdr/wrappers/python
cd ..
```
```bash
git clone https://github.com/hyperledger/aries-askar
cd aries-askar && git checkout v0.2.9
cargo build --release
cp target/release/libaries_askar.so /wrappers/python/aries_askar/bindings/libaries_askar.so
pip3.9 install -e ~/aries-askar/wrappers/python
cd ..
```
Once all the libraries have been configured and the python dependencies have been included it is possible to install the ACA-Py library.
```bash
pip3.9 install aca-py
```
### Configuring ACA-PY: Command Line Parameters

ACA-Py agent instances are configured through the use of command line
parameters, environment variables and/or YAML files. All of the configurations
settings can be managed using any combination of the three methods (command line
parameters override environment variables override YAML). Use the `--help`
option to discover the available command line parameters. There are a lot of
them--for good and bad.
