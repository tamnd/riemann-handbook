---
id: theorem-s-rec
title: Theorem S for one pair of words, from the abstract pair bound
kind: theorem
decl: Formalism.L2.SG.SpectralTiesReal.theoremS_rec
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.SpectralTiesReal
covers: 914
status: drafted
drafted_by: writer@claude
---
This theorem applies the abstract pair bound [`pbApplied`](/entry/pb-applied/) to the concrete term series $t_O(u, u')$ of two words $u \neq u'$. It gives the bound of Theorem S on $\|K_0(u,u')\|^2$, and then on the Hilbert-Schmidt norm of $K_D(u, u')$. Its only user is [`theoremS_rec2P`](/entry/theorem-s-rec2-p/). The proof is a translation: it builds the abstract inputs of `pbApplied` from the concrete hypotheses.

## Statement

Assume `LocalModelAt D`, `RowsInputP D`, and `DensInputAt D` under `LocTied D`, for each datum $D$. Let $C_4 \ge 1$ and $C_{\mathrm{thr}}$ be real. Then the constants $C_A, C, k_0$ exist as in `pbApplied`, with the same conditions on $C_0, C_G, C_\Delta, c_T, C_b$. For each datum $D$, size data $L$ with scale $b \ge 0$, Hida setting $X$, full datum $Y$ with `FinX Y`, words $u \neq u'$, size datum $G_0$ and the auxiliary data, assume:

1. the carrier condition `CarrierFull`, an isomorphism `SIso`, and that $F$ has $f$ infinite places;
2. $k_0 \le k(G_0)$, `SzHyp`, the two bounds on $C_f$, and $2r + 2 + f + 5 \le k$;
3. $T(u) \equiv T(u') \bmod g_S^2$, `PrimeHyp`, `LocTied`, irreducible $\varpi$, `Formula`, `RowLabel`, `RowsSum` and the row form `RowFormC`;
4. `MassDataHyp`, `Link` and `SplitInputs` for the mass data `massDataY`, and `SizeNumbers` with $c_5$ and $C_n$;
5. `RowBig`, `RowNotScalar` and `RowNG` for $t_O(u, u')$, with the bounds of `pbApplied` at $d = d(u) d(u') / D^*(G_0)$, and $D^*(G_0) = D^*$;
6. `KExpansion`, `AbsConvT`, `IdDegenerate`, and that the degenerate part of $t_O(u,u')$ is zero.

Then
$$\|K_0(u,u')\|^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}, \qquad \|K_D(u,u')\|_{\mathrm{HS}}^2 \le (1 + b^{-6})\, \frac{d(u)\, d(u')}{D^*}.$$

## Proof

Take $C_A$, $C$ and $k_0$ from `pbApplied`. Then, for one pair:

1. `CarrierFull` gives an abstract Hida setting $S$ with $C_A(S) = C_A$, $G(S) = G_0$, $d_e(S) = d_e$, $d_e'(S) = d_e'$, $l(S) = l$, a compatibility `Compat`, and `RealInputs`. Substitute these equalities.
2. `inst_dOf` gives `J.Inst`. `LocalModelAt` gives `LocalModel`.
3. `DensInputAt` gives `DensInput`, rewritten by `glob_f_eq`, a bound and $\alpha > 0$.
4. `RowsInputP` gives positive semidefinite rows. The row form `RowFormC` is, by definition, the identity `KVIdentity`. With `kv_nonneg` and `kv_identity_bound`, `rowsInput_of` gives `RowsInput`.
5. `energyLink_bCF` gives `EnergyLink`, after a rewrite with the count of infinite places.
6. `pbApplied` now gives the bound on $\|K_0\|^2$. Rewrite $D^*(G_0) = D^*$.
7. `packageTieConc` turns this into the Hilbert-Schmidt bound.

## In the Lean code

The theorem is at [SpectralTiesReal.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/SpectralTiesReal.lean#L147). `CarrierFull` is at line 57 of the same file. `packageTieConc` is in [ParametersTermRelations.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/ParametersTermRelations.lean#L377).

The two bounds use different forms of $b^{-6}$: `(L.sc.b ^ 6)⁻¹` with a natural power, and `L.sc.b ^ (-(6 : ℝ))` with a real power. The row form [`RowFormC`](/entry/row-form-c-of-leaves3/) is used only through the `KVIdentity` that it equals by definition.
