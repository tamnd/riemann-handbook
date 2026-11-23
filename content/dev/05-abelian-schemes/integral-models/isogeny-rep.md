---
id: isogeny-rep
title: Isogenies killed by k form a finite étale scheme
kind: theorem
decl: GlobalTheory.UPel.HT.ES.IsogRep.isogeny_rep
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsogenyRepresentableFiniteEtale
covers: 391
status: drafted
drafted_by: writer@claude
---
This theorem classifies, by a finite étale $S$-scheme $Y$, the isogenies out of an abelian scheme $A/S$ that have a quasi-inverse for an integer $k$ invertible on $S$. It is the proof of [isogeny_representable_finite_etale](/entry/isogeny-representable-finite-etale/), which [exists_rep](/entry/isog-rep-exists-rep/) uses. The classification of kernels ([its own entry](/entry/t-exists-finite-etale-trivializing-torsion-abelian-scheme/)) does most of the work; this theorem adds the quotient by the universal kernel.

## Statement

An abelian scheme is a commutative group scheme, smooth and proper with geometrically connected fibres. A *group pullback* of $A$ along $x \colon T \to S$ is a group scheme $A_1/T$ with a map $\varphi_1 \colon A_1 \to A$ that makes $A_1 = A \times_S T$ and respects the group law (`IsGrpPullback`). Homomorphisms $\psi \colon A_1 \to B_1$ and $\psi' \colon B_1 \to A_1$ are *quasi-inverse for $k$* (`IsQuasiInv k`) if $\psi' \circ \psi = [k]_{A_1}$ and $\psi \circ \psi' = [k]_{B_1}$.

**Theorem.** Let $S$ be locally noetherian, $A/S$ an abelian scheme, and $k > 0$ an integer invertible on $S$. Then there is a finite étale $Y \to S$ such that, for each group pullback $A_0$ of $A$ to $Y$, there are an abelian scheme $B/Y$ and a pair $\psi \colon A_0 \to B$, $\psi'$ quasi-inverse for $k$, with this property: for each $S$-scheme $x \colon T \to S$, each group pullback $A_1$ of $A$ to $T$, and each abelian scheme $B_1/T$ with a pair $\psi_1, \psi_1'$ quasi-inverse for $k$, there is a unique $S$-map $y \colon T \to Y$ for which $A_1 \to A_0$ and some $B_1 \to B$ are group pullbacks along $y$ that carry $\psi_1$ to $\psi$.

So $Y$ is a fine moduli space for such isogenies out of $A$, up to isomorphism of the target.

## Proof

1. [The classification of kernels](/entry/t-exists-finite-etale-trivializing-torsion-abelian-scheme/) gives $Y$, and over $Y$ a finite étale subgroup $H \subset A_0$ killed by $k$. For each $T$ and each homomorphism $f$ from $A_1$ to an abelian scheme whose kernel is killed by $k$, there is a unique $y$ with $\ker f = y^* H$.
2. $A_0$ is an abelian scheme (`isAbelianScheme_of_isGrpPullback`). `exists_quot_quasiInv` forms $B = A_0/H$ with `quotGlobal_holds`, the quotient of an abelian scheme by a finite flat subgroup. Since $H \subset A_0[k]$, the map $[k]$ factors through the quotient map $\psi$ as $\psi' \circ \psi$ (`exists_monHom_factor_of_flat_surjective`), and $\psi \circ \psi' = [k]$ follows since $\psi$ is an epimorphism. The kernel of $\psi$ is $H$.
3. Given $(T, A_1, B_1, \psi_1, \psi_1')$, the kernel of $\psi_1$ is killed by $k$, as $\psi_1' \circ \psi_1 = [k]$. Step 1 gives the unique $y$ with $\ker \psi_1 = y^* H$. `pullQuasiInv` pulls $(B, \psi, \psi')$ back along $y$ to $(B_2, \psi_2, \psi_2')$. `ker_iff_of_pullbacks` shows $\ker \psi_2 = y^* H = \ker \psi_1$. As $\psi_2$ is finite, étale and surjective (`isFinite_etale_surjective_of_isQuasiInv`), `exists_iso_of_sameKer` gives an isomorphism $\beta \colon B_1 \to B_2$ with $\beta \circ \psi_1 = \psi_2$.
4. Uniqueness: another such $y'$ has $\ker \psi_1 = y'^* H$ (`ker_iff_of_pullbacks`), so $y' = y$ by step 1.

The rest is bookkeeping.

## In the Lean code

The theorem is in [IsogenyRepresentableFiniteEtale.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsogenyRepresentableFiniteEtale.lean#L100), with `exists_quot_quasiInv` at line 39 and `ker_iff_of_pullbacks` at line 69. `IsQuasiInv` is in [ExistsQuasiInv.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsQuasiInv.lean#L11) and `QuotGlobal` in [ChainOfKernelsUnique.lean](lean:Development/AbelianVarietyTheory/Statements/PlaceShiftStatements/ChainOfKernelsUnique.lean#L17). We have not opened the proofs of `pullQuasiInv`, `exists_iso_of_sameKer` or `quotGlobal_holds`.

The hypothesis $0 < k$ is only passed to step 1, whose proof does not use it. It is redundant: if $0$ is a unit on $S$, then $S$ is empty. Only $y$ is unique, not the map $B_1 \to B$.
