---
id: main-big
title: The length bound in cases II and III from a Frobenius element
kind: theorem
decl: main_big
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.ConductorAtMapInjectiveCoeff
covers: 559
status: drafted
drafted_by: writer@claude
---
This private lemma holds the content of $\mathrm{CountII}$ and $\mathrm{CountIII}$ for the [window bound](/proof/vwin/). It bounds the length $V_{\mathrm{len}}(e, \psi)$ in case II or case III by $(l N e)^C$. Its user [`sp4Main_alt`](/entry/sp4-main-alt/) removes its two hypotheses on roots of unity. The idea: the length is at most the length `D.sha` of some raw data $D$. A Frobenius element $\sigma$ at a small auxiliary prime makes a product of trace differences nonzero, and this product bounds `D.sha`.

## Statement

Take the nine inputs of `sp4Main_alt`. Among them, `NumberSp4Alt` gives a nonzero integer whose size bounds a product of differences $\operatorname{tr} r(\sigma) - \mathrm{eis}_4$ from below. `SoV` says that an unramified cocycle that is trivial at $l$ is a coboundary. `SoFin` says that the length `Chr.V l e ψ` is finite, for $e \ge 1$ and $\psi$ with open kernel. We have not unfolded `Chr.V`. We have not unfolded `LemmaM`, `LemmaM'`, `LemmaP` or `CorX`.

**Lemma.** For each primitive character $\chi$ there is $C$ with this property. Let $h$ be a host with character $\chi$ and $h.\mathrm{Big}\ t$, $l \ne 2$ prime, $0 < e < t$, and $\psi \in h.X\ c\ e$ in case II or case III. Suppose that $\mathcal{O}_c$ has enough $2^{n_{II}}$-th and $2^{n_{III}}$-th roots of unity. Then $V_{\mathrm{len}}(e, \psi)$ is finite and $V_n(e, \psi) \log l \le (l N e)^C$.

## Proof

1. `exists_frob_nonvanishing_with_sha_bound` (from `NumberSp4Alt`) gives $C, A$. For good raw data $D$ whose characters $\psi, \xi, \omega$ kill $\mu_N$ and have order dividing $k$, and a prime $p \ge 5$ with $p \nmid N$ and $p \notin D.S$: if all irreducible pieces are `IsAut4Alt`, there is $\sigma$ with $\operatorname{tr} r(\sigma) \ne \operatorname{tr} r_0(\sigma)$ for each piece $r$. Also `D.Ineq σ` implies $\|\mathrm{sha}\| \log l \le 2 C k (N(e+1))^A \log p$.
2. `arith` bounds this right side by $(l N e)^{C'}$ for the values of $k$, $N$ and $p$ used below. Take $C'$ as the constant.
3. `dataEx` gives good raw data $D$ in the case of $(h, e, \psi)$. `SymplecticFourImageDense` gives `Fin0`, `NoEnd`, $\iota$ and the automorphy of the pieces. `shaEq` gives $V_{\mathrm{len}} \le$ `D.sha`.
4. `exModel` builds a model $M$ of $D$ from `LemmaP` and parts of `CohomologyHyp`.
5. `OfChar` fixes $n'$ and $p_1$: $n' = n_{II}$, $p_1 = 1$ in case II, and $n' = n_{III}$, $p_1 = p_1(\chi)$ in case III. `levOf` gives the conditions on $\mu_N$ and on the orders, with level $l\, 2^{n'} N p_1$.
6. Let $p$ be the least prime $p \ge 5$ with $p \nmid l N p_1$. `pZeroLe` gives $p \le 2 l N p_1 + 10$ through Bertrand's postulate (`Nat.exists_prime_lt_and_le_two_mul`). Step 1 gives $\sigma$.
7. `galoisRep_ineq_of_allIrreducible_nonvanishing` proves `D.Ineq σ`: `D.sha` is finite and $\|\mathrm{sha}\| \log l \le 2 \sum_r -\log \|\operatorname{tr} r(\sigma) - \operatorname{tr} r_0(\sigma)\|$. It uses $M$, `LemmaM`, `LemmaM'`, the local theorems, `SoV`, `SoFin`, `Fin0`, `NoEnd`, and `RigiditySymplecticFour` for each piece.
8. `Chr.nrm_mono` and $V_{\mathrm{len}} \le$ `D.sha` finish the proof.

All hypotheses of the lemma are used.

## In the Lean code

The lemma is in [ConductorAtMapInjectiveCoeff.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean#L68). `Raw.sha`, `Raw.aVal` and `Raw.Ineq` are in [DecompSigmaOrd.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/DecompSigmaOrd.lean#L186). The step lemmas are in [CountS.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/CountS.lean#L14), [TwoPowClogLe.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/TwoPowClogLe.lean#L172), [PZeroLe.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/PZeroLe.lean#L6) and [GaloisRepIneqOfAllIrreducibleNonvanishing.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/SymplecticGSp4/GaloisRepIneqOfAllIrreducibleNonvanishing.lean#L152).

The file `SymplecticGSp4/ConductorAtMapInjectiveCoeff.lean` has a second private `main_big` at line 91. It has the same proof, with `Aut.Sp4In`, `Af.NumberSp4` and `Af.AdVanishQ` in place of the `Alt` inputs and of `RigiditySymplecticFour`.
