---
id: model-on-hodge-of-family-pos
title: Hodge-Tate families give the local Chern comparison for the Hodge flag
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.HodgeModel.model_on_hodge_of_family_pos
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.ModelOnHodgeFromFamily
covers: 2528
status: drafted
drafted_by: writer@claude-opus-5-5
---
This theorem computes the local intersection numbers of the Hodge flag at a place above $p$. It assumes that Hodge-Tate lattice families exist (`FamilyExistsPos`). The answer is an explicit combination of intersection numbers on the fibre at $p$, with coefficients from the Frobenius action on the CM types. It is restated as [`model_on_hodge_from_family`](/entry/model-on-hodge-from-family/), which [`goodTower_and_volume`](/entry/good-tower-and-volume/) passes to [`volume_theorem_of_inputs`](/entry/volume-theorem-of-inputs/). Its hypothesis comes from [`family_pos_of_hodge_tate_inputs`](/entry/family-pos-of-hodge-tate-inputs/). Of the 2,528 declarations below it, [`arithmetic_relations_statement_holds`](/entry/arithmetic-relations-statement-holds/) holds the most.

## Statement

Fix a CM field $E$ with a host $H$ and a datum $D$ of signature $(p_D, q_D)$, an arithmetic variety of dimension $d+1$ with a Hodge component $\mathfrak{M}$, and a prime $p$ in the set $S$ of $\mathfrak{M}$. Assume that $\mathfrak{M}$ has no Hodge-Tate torsion at $p$, $p \neq 2$, $p \nmid \operatorname{disc} E$, and that $\varphi$ is a Frobenius at $p$ on the labels: $\varphi(s)(a) \equiv s(a)^p$ modulo each prime above $p$.

`FamilyExistsPos` says: if $p_D + q_D > 0$, then over each place above $p$ and for each label $t_0$ there is a family of Hodge-Tate lattice data. It has a finite field $F$ of characteristic $p$, a map $e$ with $t_0$ in its range and $e \circ \varphi' = \varphi \circ e$, and Lie lattice data whose de Rham and Hodge-Tate lattices match those of $\mathfrak{M}$.

**Theorem.** Assume `FamilyExistsPos`. Let $\mathrm{Fl}$ be a flag of $\mathfrak{M}$ and $T$ a local pair indexed by $\mathrm{CMType}(H) \times \mathrm{Fin}(p_D + q_D)$, such that $\mathrm{Fl}$ has two levels for $S_0 \subset S$ and $T$, with $p \notin S_0$. Let $O$ be the local ring at a place above $p$ of the integral closure of $\mathbb{Z}$ in the field $\Omega$ of the data. Then `FlagChernComparison` holds over $O$. For each $\tau$, each $k \geq 1$ and each $Q$ with $|Q| + k = d + 1$,
$$\mathrm{ck}(T|_\tau, Q) = \mathrm{cycNum}\Big(\mathrm{div}(P), T.x, \; k \sum_{\tau'} \mathrm{co}(\varphi, p, k, \tau, \tau')\, \mathrm{liePs}(k-1, \tau'), \; Q\Big),$$
where $\mathrm{co}(\varphi,p,k,\tau,\sigma) = \sum_{n} [\varphi^{n+1}\tau = \sigma]\, p^{-k(n+1)} - [\sigma = \tau]/(p-1)$.

## Proof

1. If $p_D + q_D = 0$, both sides are $0$. This case is separate because the hypothesis applies only when $p_D + q_D > 0$.
2. `arith_variety_coord_ideal` shows that $O$ is a discrete valuation ring, and `localization_model_over_place` gives a model over $O$. The hypothesis gives the families.
3. `exists_dvr_extension_field` gives an extension $O'$ of $O$ with a primitive $N$-th root of unity, $N = \prod_t (|F_t| - 1)$. The model and the function field move to $O'$.
4. `hodge_flag_outside_prime_fibres` shows that the Hodge-Tate and de Rham lattices agree away from the fibres over primes. With `hodge_flag_cm_type_degree`, `arith_variety_dedekind_constants`, `flag_pair_chart_bundle_compat` and `model_descent_valuation_fibre`, this gives lattices and frames over $O'$.
5. For each label $t$, `model_descent_generic_fibre` and `arithmetic_relations_statement_holds` give `Relations` on the orbit of $t$.
6. `local_comparison_of_orbits_holds` turns these relations into `LabelChernComparison`. This step solves the Frobenius recursion, which gives the coefficients $\mathrm{co}$.
7. `flag_m3_from_local` gives `FlagChernComparison` over $O'$, and `model_descent_integral_closure` brings it down to $O$.

## In the Lean code

The theorem is in [ModelOnHodgeFromFamily.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/ModelOnHodgeFromFamily.lean#L37). The conclusion is in [HodgeLatticeFlagBound.lean](lean:Development/AutomorphicSpectrum/Statements/GeometryStatements/HodgeLatticeFlagBound.lean#L12), and the hypothesis in [FamilyExistsPosOfFamilyExists.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FamilyExistsPosOfFamilyExists.lean#L19). The proof is about 130 lines. It calls each named lemma through its restatement in the namespace `GlobalTheory.T`. Step 7 also uses `local_number_permutation_invariant` and `dualRev_dualRev` to match the two halves of the flag.

The name `HodgeLatticeFlagBound` says "bound", but the statement is an equality.
