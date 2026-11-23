---
id: span-std
title: Bounded holomorphic forms lie in the span of theta series, for the standard source frame
kind: theorem
decl: GlobalTheory.AdSpan.span_std
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ThetaSpanAndGoodRange
covers: 719
status: drafted
drafted_by: writer@claude
---
This theorem is the case of [`span_any`](/entry/span-any/) where the source space $S$ already has Gram matrix $1$ and a context `Ctx S T` is given. It has the same conclusion: a bounded, left $G_T(\mathbb Q)$-invariant function $\varphi$ of the right level, killed by the lowering operators and with the torus weight of $\mathrm{pt}(\Delta)$, lies in the span of the theta series $g \mapsto (\omega(h,g)\,\mathrm{pt}(P))(0)$ with $P \in U$. Here the theorem does the work: it puts together the lemmas on Fock vectors, characters and holomorphy.

## Statement

Use the notation of [`span_any`](/entry/span-any/). The differences are these. A context $C$ (`Ctx S T`) gives $\psi$, $\theta$, a lattice $\Lambda$ and the signature $(p_0, q_0)$. $B_0$ is a good basis (`C.IsB`), $B_S(\tau)^* B_S(\tau) = 1$, $T$ satisfies `SigOK`, and $\Lambda_T$ is self-dual with `IsAA C.X.Λ ΛT`. $\beta_S$ is a frame of the standard lattice `stdL`. The vector $f$ satisfies `IsThPVecOf` for the Cartan matrix `C.sB B₀`. The polynomial $\Delta$ is `delta p q ap am` with $p = p_0$ and $q = q_0$ at every place. The other hypotheses on $\varphi$, $U$ and $f$ are those of `span_any`, with $B_0$ in place of the basis of $M$.

## Proof

1. [`thetaLiftFiniteVector_eq_translate_levelDatum`](/entry/theta-lift-finite-vector-eq-translate-level-datum/) writes $f = \omega(k_0,1)\, u$ with $k_0 \in G_S(\mathbb A_f)$ and $u$ = `C.uVec Lv hn f'`, a finite sum of Heisenberg translates of a base vector $f'$ for a level datum `Lv`. It also says that each element $k$ of the level group `LevK` stabilizes $\beta_T$ and reduces to $1$ on $P_g$.
2. Since $u$ is theta, Fock and nonzero, so is $f$ (by `om_pres` and `fvec_om_fin`).
3. `T.stableFockSpan_contains_rowHighestPolynomials` gives weights $c, c'$ and a row-highest polynomial $Q_0$ whose Fock vector for the reversed basis $B$ is $\mathrm{pt}(\Delta) \ne 0$. It also gives, for each row-highest $Q'$, a polynomial $P \in U$ with the same vector.
4. `T.exists_continuous_realScalar_character_weakWeil` gives a continuous unitary character $z$ of $G_T(\mathbb R)$ with the property `RealScal` for the real points. `T.realPoints_unitaryCharacter_eq_detPower` says $z = \det^m$.
5. `T.compactTorus_acts_fockVector_rowHighest` computes the torus action on $\mathrm{pt}(\Delta)$. With the hypothesis on the torus weight of $\varphi$ and `T.holomorphicUpToFactor_of_loweringKilled_torusWeight`, this gives that $\varphi$ is holomorphic of weight `wtOf c c'` up to the factor $\det^m$ (`HolUpTo`).
6. `T.mem_span_thetaSeries_of_boundedHolomorphic` puts $\varphi$ in the span of theta series of $u$ for row-highest polynomials. Its level hypothesis follows from the hypothesis on $f$ and step 1, since $\omega(1,k)$ commutes with $\omega(k_0^{-1},1)$.
7. Each theta series $g \mapsto (\omega(h,g)\,\mathrm{fvec}(Q'))(0)$ of $u$ equals the theta series of $\mathrm{pt}(P)$ for $h k_0^{-1}$, by step 3 and `fvec_om_fin`.

## In the Lean code

The theorem is at [ThetaSpanAndGoodRange.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ThetaSpanAndGoodRange.lean#L60). The helper `fvec_om_fin` is at line 49. The analytic input is in step 6 and in the character lemma of step 4; this theorem only joins them. The level clause of step 1 is needed because the hypothesis on $k$ is stated with $\beta_T$ and $P_g$, but the theta-series lemma asks for invariance under `LevK`. We did not unfold `uVec`, `HolUpTo`, `RealScal` or `wtOf`.
