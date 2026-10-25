import os

# 1. State Machine TikZ Code bổ sung Guard Condition [slot_available == True]
STATE_MACHINE = r"""
\begin{tikzpicture}[
    node distance=2.5cm and 3cm,
    state/.style={draw, rounded corners, fill=blue!10, minimum height=1cm, align=center},
    arrow/.style={->, >=stealth, thick}
]
  % Nodes
  \node [state] (pending) {Pending Confirmation\\(pending\_confirmation)};
  \node [state, right=of pending] (confirmed) {Confirmed\\(confirmed)};
  \node [state, right=of confirmed] (completed) {Completed\\(completed)};
  \node [state, below=of pending] (cancelled) {Cancelled\\(cancelled)};
  \node [state, below=of confirmed] (noshow) {No-show\\(no\_show)};

  % Transitions with Guard Conditions
  \draw[arrow] (pending) -- node[above, font=\small] {Receptionist confirms (UC-05)} 
                            node[below, font=\small, red] {[slot\_available == True]} (confirmed);
  \draw[arrow] (confirmed) -- node[above, font=\small] {Doctor completes visit (UC-03)} (completed);
  \draw[arrow] (pending) -- node[left, font=\small] {Patient cancels >2h (UC-04)} (cancelled);
  \draw[arrow] (confirmed) -- node[above, font=\small] {Patient cancels >2h (UC-04)} (cancelled);
  \draw[arrow] (confirmed) -- node[right, font=\small] {Time passed \& no arrive} (noshow);
\end{tikzpicture}
"""

# 2. DFD Level 2 TikZ Code cho Process 5.0 (Drug Safety Warning)
DFD_LEVEL2_PROC5 = r"""
\begin{tikzpicture}[
    process/.style={circle, draw, fill=orange!20, minimum size=1.6cm, align=center, font=\small},
    datastore/.style={draw, top color=white, bottom color=white, minimum width=2.5cm, minimum height=0.8cm, align=center, font=\small},
    entity/.style={rectangle, draw, fill=green!10, minimum width=2cm, minimum height=1cm, align=center},
    arrow/.style={->, >=stealth, thick}
]
  % External Entities & Processes
  \node[entity] (doctor) {Doctor};
  \node[process, right=2cm of doctor] (p51) {5.1\\Check\\Allergy};
  \node[process, right=2.5cm of p51] (p52) {5.2\\Check\\Interaction};
  \node[process, below=2cm of p52] (p53) {5.3\\Generate\\Warning};
  
  % Data Stores
  \node[datastore, above=1.5cm of p51] (d4) {D4: Patient Allergy List};
  \node[datastore, above=1.5cm of p52] (d5) {D5: Drug Interaction Catalog};

  % Data Flows
  \draw[arrow] (doctor) -- node[above, font=\scriptsize] {Prescription Info} (p51);
  \draw[arrow] (d4) -- node[right, font=\scriptsize] {Allergy Data} (p51);
  \draw[arrow] (p51) -- node[above, font=\scriptsize] {Allergy Status} (p52);
  \draw[arrow] (d5) -- node[right, font=\scriptsize] {Interaction Rules} (p52);
  \draw[arrow] (p52) -- node[right, font=\scriptsize] {Conflict Flags} (p53);
  \draw[arrow] (p53) -| node[below, font=\scriptsize, near end] {Safety Warning Alert} (doctor);
\end{tikzpicture}
"""

def generate_tikz_files():
    """Tạo các file TikZ tương ứng cho State Machine và DFD Level 2."""
    output_dir = "generated_tikz"
    os.makedirs(output_dir, exist_ok=True)
    
    # Ghi file State Machine
    with open(os.path.join(output_dir, "state_machine_guard.tikz"), "w", encoding="utf-8") as f:
        f.write(STATE_MACHINE)
        
    # Ghi file DFD Level 2
    with open(os.path.join(output_dir, "dfd_level2_proc5.tikz"), "w", encoding="utf-8") as f:
        f.write(DFD_LEVEL2_PROC5)

    print("Success: Generated state_machine_guard.tikz & dfd_level2_proc5.tikz in 'generated_tikz/'")

if __name__ == "__main__":
    generate_tikz_files()