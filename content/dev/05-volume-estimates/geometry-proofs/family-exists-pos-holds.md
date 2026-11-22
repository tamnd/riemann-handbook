---
id: family-exists-pos-holds
title: Lattice families on the charts at ramified places
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Num.FamEx.familyExistsPos_holds
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.FamilyPosOfHodgeTateInputs
covers: 1618
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `FamilyExistsPos` from five inputs about abelian schemes and $p$-divisible groups. It is the content of [its second name](/entry/family-pos-of-hodge-tate-inputs/), which [the good tower and the volume theorem, from reduced inputs](/entry/good-tower-volume-of-reduced/) uses. The hard clause is [the theorem on test points](/entry/test-pt-test-facts/).

## Statement

Let $E$ be a CM field with a host, a datum of signature $(p_D, q_D)$ with $p_D + q_D > 0$, a level and a model $Y$. Let $y_{k,j}$ be coordinates in a field $\Omega$, one block for each factor $k$. A chart $c$ picks one $j$ in each block. Let $m(c) = \prod_k y_{k, c(k)}$, and call $c$ open when $m(c) \neq 0$. Let $\mathfrak{M}$ be a `HodgeCpt`: a normal scheme over $Y$ with generic point $\operatorname{Spec}\Omega$, a semi-abelian scheme on it, and lattices $\mathrm{dR}$, $\mathrm{HT}_p$ in its Lie module. Fix bases $b$ of the generic pieces. Let $p$ be an odd prime in $S$ that does not divide $\operatorname{disc} E$, at which $\mathfrak{M}$ is `HTFree`, and let $\varphi$ be a Frobenius permutation of the labels $\mathrm{CMType} \sqcup \mathrm{CMType}$. Let $A$ be the integral closure of $\mathbb{Z}$ in $\Omega$.

**Theorem.** Assume the five inputs of [the second name](/entry/family-pos-of-hodge-tate-inputs/). Then for each localization $O$ of $A$ at a prime above $p$ that is a discrete valuation ring, and each label $t_0$, there are a finite set $\Sigma$ with a map $e$ to the labels whose image contains $t_0$, a permutation $\varphi'$ of $\Sigma$ with $e \circ \varphi' = \varphi \circ e$, a finite field $F$ of characteristic $p$, an element $w \in O$, maps $\sigma_\tau \colon F \to O/\mathfrak{m}$, and lattice data $D_c$ for each chart, such that:

1. the lattices $\mathrm{lie}$ and $W$ of $D_c$ are the coordinate lattices of $\mathrm{dR}$ and $\mathrm{HT}_p$ in the bases $b$, and $\omega$ and $\omega_{\mathrm{HT}}$ are the duals of those for the swapped labels (`IsFamilyOf`);
2. each lattice of $D_c$ is a module over the chart ring, and $v \in \Gamma_c$ gives $(m(c)/m(c'))^k v \in \Gamma_{c'}$ for some $k$ (`IsLatFamily`);
3. $p \neq 0$ and $p$ is not a unit in $O$, and $w^{p-1} = u p$ for a unit $u$;
4. on each open chart, $D_c$ satisfies the base conditions `Base`;
5. at each test point $R_C \subset C$ of an open chart and for each lift $\chi$ of $\sigma$, the base change of $D_c$ to $R_C$ satisfies `Facts`.

Clause 3 needs $p$ to be ramified in $O$: the lemma `not_isPreFamily_of_irreducible` shows that clauses 2 to 5 fail when $p \geq 3$ is irreducible in $O$.

## Proof

1. `arith_variety_hodge_prime_bound` gives $\Sigma$, $e$, $\varphi'$, $F$, $w$ and $\sigma$, with orbit conditions. Here $w = \zeta - 1$ for a primitive $p$-th root of unity $\zeta$.
2. `arith_variety_hodge_prime_degree` gives torsion data, and `arith_variety_hodge_prime_height` gives an integral model over each open chart.
3. From `FarguesHodgeTate`, `arith_variety_model_prime_bound` gives the families for $\mathrm{lie}$, $W$, $\omega$, $\omega_{\mathrm{HT}}$ and the inclusions $\mathrm{lie} \leq W \leq w^{-1}\mathrm{lie}$, $\omega_{\mathrm{HT}} \leq \omega \leq w^{-1}\omega_{\mathrm{HT}}$, and `arith_variety_model_prime_degree` gives maps $i_\tau$ with exact sequence conditions.
4. `arith_variety_hodge_prime_count` and the local lemma `gamDel_of_seqHyp` give the other clauses of `Base`.
5. `arith_variety_hodge_prime_total` and `arith_variety_model_prime_height` give the families for $M$, $\Theta$, $\Gamma$ and $\Delta$.
6. The test clause is [`ordinary_curve_hodge_prime`](/entry/ordinary-curve-hodge-prime/).

The rest is bookkeeping.

## In the Lean code

The theorem is in [FamilyPosOfHodgeTateInputs.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/FamilyPosOfHodgeTateInputs.lean#L62). Clauses 2 to 5 are the structure `IsPreFamily` in [IsPreFamilyOfLatticeFamilyTwo.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/IsPreFamilyOfLatticeFamilyTwo.lean#L19). We have not unfolded `HTFree`, `IsFrobLabels` or the chart ring.

The names of the `arith_variety_*` lemmas do not describe their statements: `arith_variety_hodge_prime_degree` gives a torsion datum, not a degree. The inputs `QuotientByFiniteFlatStatement`, `ZarhinStatement`, `HodgeTateDatumStatement` and `OrdinaryCurveStatement` are used only in the test clause.
