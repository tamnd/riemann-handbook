---
id: eigen-line-p-adic-frame
title: The p-adic norm of a line function is constant (statement form)
kind: theorem
decl: GlobalTheory.T.eigen_line_p_adic_frame
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.EigenLinePAdicFrameStatement
covers: 381
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It has the same statement as [`value_at_point`](/entry/value-at-point/), which has the real content, and its proof applies that theorem. Its user is [`finConstAll`](/entry/fin-const-all/), which builds the Hodge lattice, the bases and the order data from the flatness of a line function on the model, and then calls this theorem as its last step.

## Statement

Let $E$ be a CM field, $Y$ a model over a discrete valuation ring $O$ of a moduli space $X$ with coefficient field $F$, $Z$ a component of $Y$ over a set $U$ of points, $\tau$ a complex embedding of $E$, $p$ a prime and $\kappa \colon F \to \mathbb{C}_p$ an embedding whose unit ball is $O$. Let $\varphi$ be a line function on $U$, represented on $Z$ by the section $\alpha\, {\textstyle\bigwedge} v \,/\, \kappa'\, {\textstyle\bigwedge} w$ of the $\tau$ and $\bar\tau$ eigenspaces, and let the determinant lattice of a Hodge lattice have order $a/M$ at the uniformizer $\varpi$ along $Z$.

**Theorem.** Then there is a real $t$ such that $\log |\varphi(y, v, w)|_p = t$ for every integral framed point $y$ over a discrete valuation ring that maps to $\mathbb{C}_p$ through $\kappa$.

The precise hypotheses and the meaning of each object are in [the entry for `value_at_point`](/entry/value-at-point/).

## Proof

Apply `value_at_point`.

## In the Lean code

The theorem is in [EigenLinePAdicFrameStatement.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/EigenLinePAdicFrameStatement.lean#L11). The proof is the `first | exact @… | exact … | (intros; apply … <;> assumption)` pattern of the other statement files. The two hypotheses $\tau(r) = r_0$ and $\kappa' \neq 0$ are not used by `value_at_point` (see that entry).
