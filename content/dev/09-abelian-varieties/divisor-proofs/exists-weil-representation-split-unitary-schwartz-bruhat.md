---
id: exists-weil-representation-split-unitary-schwartz-bruhat
title: A Weil representation of a split unitary group on Schwartz-Bruhat functions (statement)
kind: theorem
decl: GlobalTheory.T.exists_weil_representation_split_unitary_schwartzBruhat
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsWeilRepresentationSplitUnitarySchwartzBruhStatement
covers: 867
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [the existence of a representation with the Kudla-Weil formulas](/entry/exists-is-kw/). Its proof applies that lemma and does nothing else. Its one user is [the Weil representation of a split unitary group, split by a character](/entry/kudla-splitting-split-unitary/), which reads off four properties of the representation.

## Statement

The setting is that of [the parent entry](/entry/kudla-splitting-split-unitary/): the quadratic extension $E/F$ of $p$-adic fields, the hermitian matrix $Q$, the characters $\psi$ and $\chi$, the group $G = U(n,n)$, and the space $S$ of locally constant functions of compact support on $X = M_{m \times n}(E)$. Let $\mu$ be an additive Haar measure on $X$.

**Theorem.** There are $\kappa \in \mathbb C$ and a representation $\omega$ of $G$ on $S$ that satisfy `IsKW`: $\omega$ is given by the explicit formula `parFun` on the Siegel parabolic $P$, and $\omega(w) = \kappa\,\mathcal F_\mu$ on the Weyl element $w = J$, where $\mathcal F_\mu$ is the Fourier transform for the pairing $\psi(\mathrm{pr}(x, y))$. The [entry for `exists_isKW`](/entry/exists-is-kw/) gives both formulas.

## Proof

The proof applies `GlobalTheory.KSp.Exist.exists_isKW` to the same arguments. There is nothing else.

## In the Lean code

The theorem is at [ExistsWeilRepresentationSplitUnitarySchwartzBruhStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilRepresentationSplitUnitarySchwartzBruhStatement.lean#L9). Its statement is word for word the statement of `KSp.Exist.exists_isKW`. The proof is a `first` tactic that tries three ways to apply `exists_isKW`. All 866 other declarations below it are below `exists_isKW`.
