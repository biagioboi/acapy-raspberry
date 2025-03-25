# Decentralized Authentication for Web of Things: a Self-Sovereign Identity (SSI)-Based Solution

For cite this work please use:

Boi, Biagio, and Christian Esposito. "Decentralized Authentication for Web of Things: a Self-Sovereign Identity (SSI)-Based Solution." 2024 International Conference on Computing, Networking and Communications (ICNC). IEEE, 2024.
```bib
@INPROCEEDINGS{10556086,
  author={Boi, Biagio and Esposito, Christian},
  booktitle={2024 International Conference on Computing, Networking and Communications (ICNC)}, 
  title={Decentralized Authentication for Web of Things: a Self-Sovereign Identity (SSI)-Based Solution}, 
  year={2024},
  volume={},
  number={},
  pages={684-688},
  keywords={Privacy;Scalability;Ecosystems;Mission critical systems;Authentication;Computer architecture;Service-oriented architecture;IoT;WoT;SSI;Authentication},
  doi={10.1109/ICNC59896.2024.10556086}}

```


Aries offers a stable and secure communication channel between two agents. In this project I want to create a Verifiable Credentials (VCs) using JSON-LD formatted credentials for creating a strong authentication for Web of Things-compliant devices.
In the example I will use the RaspberryPI as a possible node device interested in verifying his identity using VC.

## Setup, before to clone

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
## Clone
Once all the libraries have been configured and the python dependencies have been included it is possible to install the requirements for the project
```bash
pip3.9 install -r requirements.txt
```
## Running the Agent

```bash
LEDGER_URL=http://<LEDGER_URL> python3.9 main.py
```
