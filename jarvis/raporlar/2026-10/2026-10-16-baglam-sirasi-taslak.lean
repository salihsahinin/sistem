inductive Tree where
  | node (txt : List Nat) (kids : List Tree)

mutual
def Tree.L : Tree → List Nat
  | .node t ks => t ++ Tree.Ls ks
def Tree.Ls : List Tree → List Nat
  | [] => []
  | k :: ks => k.L ++ Tree.Ls ks
end

theorem Ls_eq_flatten_map (ks : List Tree) :
    Tree.Ls ks = (ks.map Tree.L).flatten := by
  induction ks with
  | nil => rfl
  | cons k ks ih => simp [Tree.Ls, ih]

def chain : List (List Nat) → Tree
  | [] => .node [] []
  | [c] => .node c []
  | c :: cs => .node c [chain cs]

theorem chain_L (cs : List (List Nat)) :
    (chain cs).L = cs.flatten := by
  induction cs with
  | nil => simp [chain, Tree.L, Tree.Ls]
  | cons c cs ih =>
    cases cs with
    | nil => simp [chain, Tree.L, Tree.Ls]
    | cons d ds => simp [chain, Tree.L, Tree.Ls] at ih ⊢; rw [ih]
