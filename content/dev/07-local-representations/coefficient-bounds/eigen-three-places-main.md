---
id: eigen-three-places-main
title: The pointwise bound for Capelli eigenfunctions from three places
kind: theorem
decl: GlobalTheory.EigenThreePlaces.main
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.CapelliEigenfunctionBoundThreePlaces
covers: 349
status: drafted
drafted_by: writer@claude
---
This theorem bounds a decaying Capelli eigenfunction $f$ at each point of the place datum $p$ by its $L^2$ size. It uses two more place data $p_+$ and $p_-$ with shifted types. The proof is an assembly: it checks the limit and growth inputs of a jet bound and then applies that bound. The restatement [`T.capelli_eigenfunction_bound_three_places`](/entry/capelli-eigenfunction-bound-three-places/) passes it to [`BpEigen.pointwise_bound_eigenfunction`](/entry/pointwise-bound-eigenfunction/).

## Statement

We use the notation of [the parent entry](/entry/pointwise-bound-eigenfunction/) for $E_f$, $G_p$ and $\|f\|^2$. Let $n = 2r+k+1$. The data $p_\pm$ have the parameter $P$ of $p$ with the types replaced by $u_\pm, u'_\pm$ (`shP`).

**Theorem.** Assume `BesselXiIntegrable`, `ThmPActualCpt` and `NFTopDomAll`. For all $C_b$ and $C_3, C_\Lambda, C_0 \ge 0$ there are $C_4, C_c$ such that the bound

$$E_f(\gamma) \le b^{C_4(2r+2)^4}\, G_p(\gamma)^{-(2p_0+n_0)}\, \|f\|^2 \qquad (G_p(\gamma) > 0)$$

holds whenever:

1. $b \ge 3$, $1 \le \Lambda \le b^{C_\Lambda(2r+2)}$, $n_0 \le 30(r+1)^2+6$, $p_0 \le C_0(r+1)^2$, $K \ge 3$ and $(r+1)K \le N \le 2p_0$;
2. $p_\pm$ have the base points $z, z'$ of $p$ and satisfy `InDDplus2` with $C_b$;
3. $f$ is smooth on $G$ and decays with rate $A_0$ in all derivatives (`InCC`);
4. $A_\pm$ are polynomial operators of coefficient degree at most $d$ (`PolyOp`), and `AmapsSh` holds: the given point maps $B_\pm$ satisfy, at each point $\gamma$ with $G_p(\gamma) > 0$, $V_{p_\pm}(f A_\pm)(\gamma) = V_p f(\gamma)\, B_\pm(\gamma)$, $\|v\|^2 \le (3b)^{2n_0}(T_q/G_p)^{n_0}(\|B_+^*v\|^2 + \|B_-^*v\|^2)$ and $\|B_\pm\|^2 \le (G_p/T_q)^{n_0}$, with $T_q$ = `Tq p`;
5. the decay margin $C_c(r+1)^4(Nn^2+n^3) \le A_0 - (2r+2)p_0 - d$;
6. `RegularityBoundBigCell` with exponent $2p_0+n_0$, and `WaveGrid`, `LiftGrid` for $p_\pm$;
7. $\mathcal{C}(y)f = \prod_s(y+\lambda'_s)f$, with $2c \le |\lambda_s-\lambda_t|$ for $s \ne t$ and $|\lambda'_s-\lambda_s| + (2r+2)p_0 + d \le c-1$;
8. $\prod_s(|y+\lambda_s|+c) \le \nu_\pm(y)$, with $\nu_\pm > 0$.

## Proof

Fix a cutoff $\chi = \sigma(2x-1)$, with $\sigma$ the smooth transition of Mathlib (`exists_isCut0`). Put $F_\pm(g) = G_f(g)^{p_0}\, f(g) A_\pm(g)$ (`fpmSh`), with $G_f$ built from the base points of $p_\pm$.

1. `T.jetBound_equalTypes_threePlaces_of_xiIntegrable` gives $C_4$ and $C_c$. It asks for three inputs on $F_\pm$, which the other steps supply.
2. `T.tendsto_levelZero_form_cutoff_pow_mul_of_domination` gives $C_n$ and `LimEvT`: for admitted words of length at most $N$, the level zero form of the cut-off $F_\pm$ tends to that of $F_\pm$. This uses $N \le 2p_0$.
3. The second part of `T.levelZeroEnergyBound_decayingCasimirEigenfunction` gives `LimBd`: the level zero form of $F_\pm$ is at most $\mathrm{normC}(\nu_\pm, w)\,\beta(F_\pm, F_\pm)$.
4. `T.latticeSum_of_compactCoefficient_positivity` gives `BlockGrowthBound` for each smooth compact approximation of the cut-off $F_\pm$.

Take $C_c' = \max(3, C_c, C_n)$. `decay_split` splits the margin for $C_c'$ into the margins for $C_c$, for $C_n$ and the bound $B.AB(k,r) \le A_0 - (2r+2)p_0 - d$ that step 3 needs.

## In the Lean code

The theorem is in [CapelliEigenfunctionBoundThreePlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/CapelliEigenfunctionBoundThreePlaces.lean#L53). `exists_isCut0` is at line 16 and `decay_split` at line 22. We have not unfolded `Tq`, `WaveGrid`, `LiftGrid`, `InDDplus2`, `BlockGrowthBound` or the Capelli operator `Q.CV`.

`NFTopDomAll` is used only in step 2. The jet bound has "equalTypes" in its name, but its statement puts no condition on the types, and this theorem also serves the case of different types.
