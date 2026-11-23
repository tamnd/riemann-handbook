---
id: kudla-splitting-split-unitary-of-literature
title: The Weil representation of a split unitary group, split by a character
kind: theorem
decl: UpperTheory.LiteratureTheorems.kudla_splitting_split_unitary_of_literature
module: Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin
covers: 1019
status: drafted
drafted_by: writer@claude
---
This theorem is a renaming. It takes the argument $O$, ignores it, and returns the theorem [`kudlaSplittingSplitUnitary`](/entry/kudla-splitting-split-unitary/), which has the real content (1,018 of the 1,019 declarations below this one). Its result fills the field `kudlaSplittingSplitUnitary` of the bundle [ThetaLocalInputs](/step/published-results-first/).

## Statement

Let $F$ be a non-archimedean local field of characteristic $0$ and $E/F$ a quadratic extension with nontrivial automorphism $x \mapsto \bar x$. Let $Q$ be an invertible Hermitian $m \times m$ matrix over $E$. Let $\psi$ be a nontrivial continuous unitary character of $F$. Let $\chi$ be a continuous unitary character of $E^\times$ with $\chi|_{F^\times} = \eta^m$, where $\eta$ is $1$ on the norms $N(E^\times)$ and $-1$ off them. Let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ of size $2n$, and let $G = \{g \in \mathrm{GL}_{2n}(E) : g^{\mathsf T} J \bar g = J\}$, a split [[unitary group|0R9R0Y1HDK]]. Let $S$ be the space of locally constant functions of compact support on $X = M_{m \times n}(E)$.

Then there is a representation $\omega$ of $G$ on $S$ such that:

1. $\omega$ is smooth: each vector has an open stabilizer;
2. $\omega(g)$ preserves the $L^2$ norm for each Haar measure on $X$;
3. $H(w)\,\omega(g) = \omega(g)\,H(wg)$ for each $w = (w_1, w_2) \in M_{m \times 2n}(E)$ with $w_1, w_2 \in X$, where $H(w)$ is the [[Heisenberg group|ZZYCV5EX9J]] operator $(H(w)\varphi)(x) = \psi\bigl(\langle x, w_2 \rangle + \tfrac12 \langle w_1, w_2 \rangle\bigr)\varphi(x + w_1)$, with $\langle \cdot, \cdot \rangle$ half the trace to $F$ of the Hermitian form built from $Q$ and $J$;
4. for $a \in \mathrm{GL}_n(E)$ and $m(a) = \operatorname{diag}\bigl(a, (\bar a^{-1})^{\mathsf T}\bigr)$, $(\omega(m(a))\varphi)(x) = \chi(\det a)\,\lvert N(\det a) \rvert_F^{m/2}\,\varphi(xa)$.

This has the shape of the [[Weil representation|H3Q2703KKV]] of $U(n,n)$ in the Schrödinger model, made linear by the splitting character $\chi$ of Kudla (Israel J. Math. 87, 1994). The statement does not fix $\omega$ on the unipotent radical or on the Weyl element, and it does not say that $\omega$ is unique.

## Proof

The proof is `GlobalTheory.kudlaSplittingSplitUnitary`, with no change.

## In the Lean code

The theorem is at [EveryCharacterOfLiteratureOfVWin.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L449). The statement `KudlaSplittingSplitUnitary` is at [KudlaSplittingSplitUnitary.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/KudlaSplittingSplitUnitary.lean#L223).

- The argument $O$ is not used.
- The quadratic extension is given by an automorphism $c$ and an element $\delta$ with $c(\delta) = -\delta$ such that $1, \delta$ is a basis (`IsQuad`). The condition on $\chi$ is `ResEtaPow ⊥ χ m`.
