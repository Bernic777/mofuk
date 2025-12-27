# Mofuk

> *To vanish is not to escape — it is to exist without unnecessary trace.*

Mofuk is a lightweight, meditative **Tor identity rotation tool** inspired by the philosophy of the **Moi Tribe of West Papua** — a way of life centered on balance, restraint, and leaving minimal footprints.

This project is designed for **privacy research**, **defensive security testing**, and **ethical network hygiene**. Mofuk does not seek domination, exploitation, or noise. It rotates identities quietly, deliberately, and consciously.

---

## ✨ Philosophy

The word **Mofuk (Moi)** means:

> *To vanish / To disappear / To be no longer visible*

In a digital world obsessed with visibility, Mofuk embraces the opposite:

- Minimal footprint over maximal reach
- Silence over noise
- Awareness over aggression

Mofuk is a reminder that privacy is not an attack — it is a boundary.

---

## 🔐 What Mofuk Is (and Is Not)

### ✔️ Mofuk **IS**
- A Tor identity rotation utility
- A privacy-awareness tool
- A defensive security research aid
- A calm, minimal CLI program

### ❌ Mofuk **IS NOT**
- An exploitation framework
- A hacking toolkit
- A vulnerability scanner
- A tool for bypassing laws or ethics

---

## 🧩 Features

- 🔄 Controlled Tor identity rotation
- 🧘 Meditative execution flow (no aggressive loops)
- 🧠 Conscious delays to reduce network noise
- 🪶 Lightweight and minimal dependencies
- 🖥️ Simple CLI interface

---

## 📦 Installation

### From PyPI

```bash
pip install mofuk
```

### From Source

```bash
git clone https://github.com/Bernic777/mofuk.git
cd mofuk
pip install .
```

---

## 🚀 Usage

Basic execution:

```bash
mofuk
```

> Mofuk assumes a running Tor service and appropriate SOCKS configuration.

Example with Tor running locally:
- SOCKS: `127.0.0.1:9050`
- ControlPort: `127.0.0.1:9051`

---

## ⚙️ How It Works (High-Level)

1. Establishes a connection through Tor
2. Requests a new identity via Tor control signals
3. Applies intentional pauses to avoid aggressive behavior
4. Resumes network activity with a fresh circuit

No exploitation. No scanning. No forced behavior.

---

## 🛡️ Security & Ethical Use

Mofuk does **not** exploit vulnerabilities and is **not intended for offensive use**.

This tool is built for:
- Defensive security research
- Privacy education
- Responsible anonymity practices

If your intent is to cause harm, create noise, or bypass ethical boundaries — **do not use this tool**.

---

## 🧪 Dependencies

- Python ≥ 3.6
- `requests`
- `requests[socks]`

> Always keep dependencies updated and monitor CVE advisories for underlying libraries.

---

## 🌱 Cultural Note

The Moi Tribe of West Papua has long practiced a way of living that respects forests, silence, and balance.

Mofuk is **not a representation** of the tribe, but an inspiration — a technical reflection of restraint and sustainability in the digital realm.

---

## 🤍 Closing

Privacy is not disappearance.
It is the right to exist without being harvested.

*Vanish quietly.*
