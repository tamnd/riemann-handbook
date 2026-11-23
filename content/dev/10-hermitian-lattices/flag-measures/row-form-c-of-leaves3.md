---
id: row-form-c-of-leaves3
title: The row form of the mass constant, from its leaves
kind: theorem
decl: Formalism.L2.SG.Pf.rowFormC_of_leaves3
module: Formalism.LocalToGlobal.SiegelLatticeTheory.FlagStabilizerTensors.RootLatticeThresholds.RowFormAllOf
covers: 326
status: drafted
drafted_by: writer@claude
---
This theorem proves the row form `RowFormC` for one pair of words $u \neq u'$ of a Hida setting. The row form writes the constant $K_V$ of the mass data as a sum of squared norms of row vectors. [`rowFormAllP_of`](/entry/row-form-all-p-of/) calls it at each selected tie and so proves `RowFormAllP`, one of the [nineteen hypotheses of Theorem S](/entry/theorem-s-leaves-of-carrier-g/). In [`theoremS_rec`](/entry/theorem-s-rec/) the row form is used as the identity `KVIdentity` of the mass data.

## Statement

Fix a datum $D$, a Hida setting $X$ with an adelic bridge, a full datum $Y$ over $X$, words $u, u'$, and the auxiliary data $X_0, \psi, s_d, C, T_h, Q, i_0, i_0', \nu_q$. Let $\mathcal B$ be the mass data `bCF` that they define, with the reals $c_0, c_0', n_{0c}, K_V$. Let $\kappa$ label the terms by natural numbers, and let $n_c$ be real. A term $t$ is *eligible* if it is generic and $G(t) \neq 0$. For a label $\rho$ put
$$R_\rho = \sum_p r_\rho(p)\, V_t(p),$$
where $p$ runs over the points, $V_t(p)$ is the vector `VtPt`, and $r_\rho(p)$ (`rowVec`) is the sum of $\sqrt{m(t)}\, c(t, w)$ over the eligible terms $t$ at the point $w$ of $p$ with $\kappa(t) = \rho$, divided by $\sqrt{n_0(w)}\,\varphi(p)$.

**Theorem.** Assume:

1. $\kappa$ is a row label: two eligible terms have the same label if and only if they are scalar to each other (`TermScal`);
2. $i_0 = i_0'$, a point representative exists (`PtRepExists`), and $\nu_q$ is pinned (`NuQPin`);
3. $2r + 2 + f + 5 \le k$ for the rank data $r, f, k$ of $D$;
4. the term series converges absolutely (`AbsConvT`);
5. the two numbers $g_0, g_1$ of the host are at least 3 and unramified in $E$;
6. `PhaseTieC`, `VolumeOddGeneric`, `PrimeHyp`, `NormRepExists`, `VIndepAtC` and `LocTied`;
7. the normalization `NcTieC`: $n_c = n_{0c}\, g_{\mathrm{ng}} / (a_l\, \kappa_N)$;
8. $\mathrm{vol}(K_2) > 0$, $c_0 c_0' > 0$, $n_c > 0$ and $\prod_q \alpha_D(q) > 0$.

Then $\sum_\rho \|R_\rho\|^2$ converges and
$$c_0\, c_0'\, K_V = n_{0c} \sum_\rho \|R_\rho\|^2.$$

We have not unfolded the conditions in item 6.

## Proof

The last step is `rowFormC_of`, which is algebra. It needs five facts.

1. `SigRowsC`: $c_0 c_0' \Sigma = \sum_\rho \|v_\rho\|^2$, where $v_\rho$ (`clsVec`) is the class vector of the label $\rho$ and $\Sigma$ is `SigOf` of the term series. `sigRowsC_of` proves it from a regrouping of rows (`rowRegroupC_of`), the class frame (`classFrameC_all`), the torsor property (`torsorC_of`) and absolute convergence on classes (`classAbsC_of`).
2. `RowVecC`: each $R_\rho$ is $\bigl(g_{\mathrm{ng}}/(\kappa_N\, n_c \prod_q \alpha_D(q)\, m_{\mathrm{rows}})\bigr)^{1/2} v_\rho$. This is `rowVecC_of`, with the weight constant `weightConstC_of` and `pointRegroupC_of`.
3. `RhoTieC`: $\rho_0 = m_{\mathrm{rows}}$, by `RhoTieC_holds`.
4. `AlTieC`: $a_l = \prod_q \alpha_D(q)$, by `AlTieC_of_loc` from `LocTied` and item 3.
5. The hypothesis `NcTieC`.

Since $K_V = \Sigma / \rho_0$ by definition, `rowForm_alg` gives the identity. Several inputs come from lemmas with no hypotheses: `iotaDictC_holds`, `relCharC_holds`, `atSomeAll_holds`, `LiftMassC_holds`, `LemmaVLiftC_holds` and `dual_frame_at_places`.

## In the Lean code

The theorem is at [RowFormAllOf.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RootLatticeThresholds/RowFormAllOf.lean#L108). `RowFormC` is in [MassDataForm.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/MassDataForm.lean#L29). `rowFormC_of`, `SigRowsC`, `RowVecC`, `AlTieC` and `rowForm_alg` are in [RowFrameCoherence.lean](lean:Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts/RankPointCounts/RowFrameCoherence.lean#L133).

Each hypothesis is used. The suffix "leaves3" suggests a third version, but no `rowFormC_of_leaves` or `rowFormC_of_leaves2` is in the source.
