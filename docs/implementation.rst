Implementation
==============

CoherentUnit
--------------------------------

VM6502Q Opcodes
---------------
This extension of the MOS 6502 instruction set honors all legal (as well as undocumented) opcodes of the original chip. See a reference manual on the 6502 for the classical opcodes.

The accumulator and X register are replaced with qubits. The Y register is left as a classical bit register. A new "quantum mode" and number of new opcodes have been implemented to facilitate quantum computation.

The quantum mode flag takes the place of the unused flag bit in the original 6502 status flag register. When quantum mode is off, the virtual chip should function exactly like the original MOS 6502, so long as the new opcodes are not used. When the quantum mode flag is turned on, the operation of the other status flags changes. An operation that would reset the "zero," "negative," or "overflow" flags to 0 does nothing. An operation that would set these flags to 1 instead flips the phase of the quantum registers if the flags are already on. In quantum mode, these flags can all be manually set or reset with supplementary opcodes, to engage and disengage the conditional phase flip behavior. The "carry" flag functions in addition and subtraction as it does in the original 6502, though it can exist in a state of superposition. A "CoMPare" operation overloads the function of the carry flag in the original 6502. For a "CMP" instruction in the quantum 6502 extension, the carry flag analogously flips quantum phase when set, if the classical "CMP" instruction would usually set the carry flag. The intent of this flag behavior, setting and resetting them to enable conditional phase flips, is meant to enable quantum "amplitude amplification" algorithms based on the usual status flag capabilities of the original chip.

Bellow is a list of new and modified opcodes with their binary and function. If an opcode description is not here to specifically state that the opcode collapses register or flag superposition, it can be assumed that it does not. However, if a (non X register indexed) instruction would overwrite the value of a register or flag, then superposition would be expected to be overwritten. If an instruction is X register indexed, then in quantum mode, it will operate according to the superposition of the X register.

HAA, 0x02, (Implied addressing)
Bitwise Hadamard on the Accumulator

HAX, 0x03, (Implied addressing)
Bitwise Hadamard on the X Register

ORA, (Multiple instructions for addressing modes)
Bitwise OR with the Accumulator, will also collapse the quantum state of the Accumulator

ASL, (Multiple instructions for addressing modes)
Arithmetic Shift Left, will also collapse superposition of the carry flag

SEN, 0x0F, (Implied addressing)
SEt the Negative flag

PXA, 0x12, (Implied addressing)
Apply a bitwise Pauli X on the Accumulator

PXA, 0x13, (Implied addressing)
Apply a bitwise Pauli X on the X Register

HAC, 0x17, (Implied addressing)
Apply a Hadamard gate on the carry flag

PYA, 0x1A, (Implied addressing)
Apply a bitwise Pauli Y on the Accumulator

PYA, 0x1B, (Implied addressing)
Apply a bitwise Pauli Y on the X Register

CLQ, 0x1F, (Implied addressing)
CLear Quantum mode flag

AND, (Multiple instructions for addressing modes)
Bitwise AND with the Accumulator, will also collapse the quantum state of the Accumulator

BIT, (Multiple instructions for addressing modes)
The 6502's test BITs opcodes, will also collapse the superposition of the Accumulator

ROL, (Multiple instructions for addressing modes)
ROtate Left, will also collapse superposition of the carry flag

SEV, 0x27, (Implied addressing)
SEt the oVerflow flag

SEZ, 0x2B, (Implied addressing)
SEt the Zero flag

CLN, 0x2F, (Implied addressing)
CLear the Negative flag

PZA, 0x32, (Implied addressing)
Apply a bitwise Pauli Z on Accumulator

PZA, 0x33, (Implied addressing)
Apply a bitwise Pauli Z on the X Register

RTA, 0x3A, (Implied addressing)
Bitwise quarter rotation on |1> axis for Accumulator

RTX, 0x3B, (Implied addressing)
Bitwise quarter rotation on |1> axis for the X Register

SEQ, 0x1F, (Implied addressing)
SEt the Quantum mode flag

EOR, (Multiple instructions for addressing modes)
Bitwise EOR with the Accumulator, will also collapse the quantum state of the Accumulator

RXA, 0x42, (Implied addressing)
Bitwise quarter rotation on X axis for Accumulator

RXX, 0x43, (Implied addressing)
Bitwise quarter rotation on X axis for the X Register

LSR, (Multiple instructions for addressing modes)
Logical Shift Right, will also collapse superposition of the carry flag

CLZ, 0x47, (Implied addressing)
CLear the Zero flag

RZA, 0x5A, (Implied addressing)
Bitwise quarter rotation on Z axis for Accumulator

RZX, 0x5B, (Implied addressing)
Bitwise quarter rotation on Z axis for the X Register

RZX, 0x5B, (Implied addressing)
Bitwise quarter rotation on Z axis for the X Register

FTA, 0x62, (Implied addressing)
Quantum Fourier Transform on Accumulator

FTX, 0x63, (Implied addressing)
Quantum Fourier Transform on the X register

ADC, 0x75, (Zero page X addressing)
ADd with Carry, Zero Page indexed, will add in superposition if the X register is superposed. Results in the Accumulator and carry flag become entangled with the X register, such that the result of the addition is entangled with the address loaded from in the X register. (Addressing past the zero page loops to the start.)

ADC, 0x7D, (Absolute X addressing)
ADd with Carry, Zero Page indexed, will add in superposition if the X register is superposed. Results in the Accumulator and carry flag become entangled with the X register, such that the result of the addition is entangled with the address loaded from in the X register.

STA, (Multiple instructions for addressing modes)
STore Accumulator, will also collapse superposition of the Accumulator

TXA, 0x8A, (Implied addressing)
Transfer X register to Accumulator, will maintain superposition of the X register, entangling it to be the same as the Accumulator when measured

STX, (Multiple instructions for addressing modes)
STore X register, will also collapse superposition of the X register

TXS, 0x9A, (Implied addressing)
Transfer X register to Stack pointer, will also collapse superposition of the X register

TAY, 0xA8, (Implied addressing)
Transfer Accumulator Y register, will also collapse superposition of the Accumulator

TAX, 0x8A, (Implied addressing)
Transfer Accumulator to X register, will maintain superposition of the Accumulator, entangling it to be the same as the X register when measured

LDA, 0xB5, (Zero page X addressing)
LoaD Accumulator, Zero Page indexed, will load in superposition if the X register is superposed. Results loaded in the Accumulator become entangled with the X register, such that the result of the load is entangled with the address loaded from in the X register. (Addressing past the zero page loops to the start.)

LDA, 0xBD, (Absolute X addressing)
LoaD Accumulator, Zero Page indexed, will load in superposition if the X register is superposed. Results loaded in the Accumulator become entangled with the X register, such that the result of the load is entangled with the address loaded from in the X register.

CMP, (Multiple instructions for addressing modes)
CoMPare accumulator. If quantum mode is off, this opcode functions as in the original 6502. If quantum mode is on, and if a flag would be set to 1 in the original system, and if this flag is already on, then this instead flips the phase of the quantum registers, for each such flag.

CPX, (Multiple instructions for addressing modes)
CoMPare X register. If quantum mode is off, this opcode functions as in the original 6502. If quantum mode is on, and if a flag would be set to 1 in the original system, and if this flag is already on, then this instead flips the phase of the quantum registers, for each such flag.

SBC, 0xF5, (Zero page X addressing)
SuBtract with Carry, Zero Page indexed, will subtract in superposition if the X register is superposed. Results in the Accumulator and carry flag become entangled with the X register, such that the result of the addition is entangled with the address loaded from in the X register. (Addressing past the zero page loops to the start.)

QZZ, 0xF7, (Implied addressing)
Apply Pauli Z operator to zero flag

QZS, 0xFA, (Implied addressing)
Apply Pauli Z operator to negative flag

QZC, 0xFB, (Implied addressing)
Apply Pauli Z operator to carry flag

SBC, 0xFD, (Absolute X addressing)
SuBtract with Carry, Zero Page indexed, will subtract in superposition if the X register is superposed. Results in the Accumulator and carry flag become entangled with the X register, such that the result of the addition is entangled with the address loaded from in the X register.

CC65
----

.. _c-syntax-enhancements-ref:

C Syntax Enhancements
~~~~~~~~~~~~~~~~~~~~~

