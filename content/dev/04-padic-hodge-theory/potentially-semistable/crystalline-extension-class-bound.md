---
id: crystalline-extension-class-bound
title: The crystalline extension class bound, as a named statement
kind: theorem
decl: GlobalTheory.T.crystalline_extension_class_bound
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CrystallineExtensionClassBoundStatement
covers: 620
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the class bound](/entry/class-bound/). It gives the first half of `Conclusion4` in [the assembly of the two local torsion statements](/entry/tb-assembled/). The content is in the class bound.

## Statement

Let $D$, $HW$, $F$ be as in [the assembly](/entry/tb-assembled/). Suppose `admitted D HW F`. Then for every prime $\ell$, finite extensions $K$, $L$ of $\mathbb{Q}_\ell$ and $s \geq 1$ with `Good K s L`, the statement `TBat S E` holds for the local situation $S$ of these data.

In words: let $0 \to Y \to \tilde Y \to Z \to 0$ be an exact sequence of lattice representations of $G_K$ with $Z$ trivial and $\tilde Y$ crystalline, and let $\varphi$ be a $G_K$-map from the lattice of $Y$ to $V_e/T_e$, where $G_K$ acts on the line $V_e$ by $\chi^{-e}$. Then a fixed power $\ell^c$ times the push-forward by $\varphi$ of the extension class lies in the Bloch-Kato group $H^1_f(K, V_e/T_e)$. The exact hypotheses and the value of $c$ are in [the class bound](/entry/class-bound/).

## Proof

The proof is one line, `first | exact @GlobalTheory.Cyc.ClassBound.class_bound | ...`. The first branch applies, since the statements are the same.

## In the Lean code

The theorem is in [CrystallineExtensionClassBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBoundStatement.lean#L9). It calls `GlobalTheory.Cyc.ClassBound.class_bound` only. `TBat` is defined in [LocalSituation.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L165).
