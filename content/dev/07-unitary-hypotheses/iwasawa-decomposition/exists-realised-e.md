---
id: exists-realised-e
title: A concrete theta datum from automorphic forms
kind: theorem
decl: GlobalTheory.Mem.TrueRecordEq.exists_realisedE
module: Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsRealisedE
covers: 404
status: drafted
drafted_by: writer@claude
---
This theorem builds the theta datum that [`exists_allTied_eqTied_on`](/entry/exists-all-tied-eq-tied-on/) needs. It takes the abstract model `ThetaX D` and fills each field with a true object: automorphic functions on adelic unitary groups, the Petersson integral, theta integrals and Bessel periods. Here is the place where the abstract theta datum meets analysis.

## Statement

Let $D$ be a datum. Assume five integrability statements, all of which the caller gets from rapid decay of cusp forms:

- `PetInt`: for a fundamental domain $\mathcal{F}$ of $U(V)(F)$ in $U(V)(\mathbb{A})$, the function $\overline{\varphi}\,\varphi'$ is integrable on $\mathcal{F}$ when $\varphi$ is a smooth automorphic function and $\varphi'$ is a cusp form;
- `TopInt`: the same along an isometric embedding $B \to A$;
- `BesInt`: the integrals that define the Bessel periods converge;
- `LiftAut` and `LiftAutEq`: for an admitted pair $(V, W)$ with characters $\chi, \chi'$, the theta integral
$$h \mapsto \int_{\mathcal{F}} \omega(g,h)\Phi(0)\, F(g)\, d\mu(g)$$
of a cusp form $F$ on $U(V)$ converges and is a smooth automorphic function on $U(W)$. `LiftAut` is for the Weil function $W_f$, and `LiftAutEq` is for each Weil representation in the equal rank case.

**Theorem.** For each infinity type $\theta$, each standard $\psi$ of sign $-1$, each Weil function $W_f$ for $\psi$ of equal rank, each tower $T_w$ and each record of functions $R$, there are a theta datum $X$, a tie $T$ to automorphic functions, a Weil tie $W$ with $W.\psi = \psi$, and a Bessel tie $B$, such that $B$ realises $W_f$, $T_w$ and $R$ (`RealisesE`).

## Proof

The proof gives the construction `recXE` and shows that each field agrees with the input. Most checks are `rfl`. For each Hermitian space $V$ of $D$:

1. The space of $V$ is the span of the smooth automorphic functions of type $\theta$ on $U(V)(\mathbb{A})$, and the cuspidal subspace is its intersection with the space `CuspS` of cusp forms (`AFs` and `cuspIn`).
2. The Petersson form is $c_V \int_{\mathcal{F}} \overline{F}\,G\, d\mu$, with $c_V$ the constant `petC` of $R$. It is positive by `petersson_normSq_pos_automorphicFunction_unitary` and the positivity of the local constants of $R$.
3. The real and finite places act by right translation.
4. The characters are the Hecke characters of $E$. The Schwartz spaces are those of $\psi$.
5. The theta lift from $V$ to $W$ is $c_V$ times the theta integral above. `exists_liftE` (line 30) gives it as a bilinear map. It is $0$ when the pair is not admitted or the signature of $V$ is wrong. The integral does not depend on the choice of $\mathcal{F}$, because the kernel is left invariant (`ker_leftE`, line 20).
6. The Bessel periods are $c_A$ times the period integrals, and the constant `besC` of the Bessel tie is $1$.
7. The tower, the rows, the columns, the maps $\Phi$ and the constants $m_Y$ come from $T_w$ and $R$ without change.

## In the Lean code

The theorem is in [ExistsRealisedE.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsRealisedE.lean#L312). The integrability statements are in [AdelicDataRowMeasureScaleTrivialTuple.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/AdelicDataRowMeasureScaleTrivialTuple.lean#L623), and `LiftAutEq` and `RealisesE` are in [ExistsSplittingCharacterSelf.lean](lean:Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsSplittingCharacterSelf.lean#L128).

The construction is `recXE`, with `recTE`, `recWE`, `recKE` and `recBE`; `realisesE` (line 270) checks the fields. The proof of the theorem is one line. We have not unfolded `CuspS`, `perT` or `RecFun`, and we have not read every field of `RealisesE`.

Odd point: the Petersson form, the theta lifts and the Bessel periods all carry the factor $c_V$ from $R$. So the normalisation of the theta datum comes from the record $R$, not from the construction.
