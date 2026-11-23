---
id: eig-inert
title: Iwahori eigenvalues of an unramified representation at an inert place
kind: theorem
decl: PositivityTheory.Rg.BcB.F.Eig.eigInert
module: Development.WeilBound.RepresentationTheoryGL.ArchimedeanBaseChange.ArchimedeanBaseChangeProof.SatakeExponents.UniformizerValuations.InertEigenvalues.EigInert
covers: 1033
status: drafted
drafted_by: writer@claude
---
Let $\sigma$ be an unramified representation of a unitary group at a place that is inert in a CM extension. This theorem gives a nonzero Iwahori fixed vector and its Iwahori-Hecke eigenvalues in terms of the Satake parameters. Its one caller is [frame existence from finiteness](/entry/frame-ex-of-fin/), through `coneEigOf`.

## Statement

Let $E$ be a CM field and $w$ a finite place of $E$ that is not split (`IsSplitAt`, not unfolded). Let $\bar x$ be conjugation on $E_w$ (`cj w`) and $g^* = \bar g^{\mathsf T}$. Let $U = \{g \in \mathrm{GL}_n(E_w) : g^* g = 1\}$ and $U' = \{g : g^* J g = J\}$, with $J$ the antidiagonal matrix of ones. Let $m = \lfloor n/2 \rfloor$. The hypotheses are:

- $b \in \mathrm{GL}_n(\mathcal{O}_w)$ with $b^* b = J$;
- $\varpi$ is a uniformizer of $E_w$ with $\bar\varpi = \varpi$;
- conjugation is nontrivial on the residue field, of order $q^2$ (`IsUnramInv`);
- $\sigma$ is a smooth irreducible admissible representation of $U$;
- $\sigma$, moved to $U'$ by $g \mapsto b^{-1} g b$, is spherical for $U' \cap \mathrm{GL}_n(\mathcal{O}_w)$ with Satake parameters $\alpha \in (\mathbb{C}^\times)^m$ (`SatUL`, `HasSatU`).

For $l \in \mathbb{Z}^m$ let $t_l = \mathrm{diag}(\varpi^{l_1}, \dots, \varpi^{l_m}, 1, \dots, 1, \varpi^{-l_m}, \dots, \varpi^{-l_1})$. Call $l$ a cone point if $l_i \ge 2$ and $l_i - l_{i+1} \ge 2$ for all $i$. Let $I_0$ be the standard Iwahori subgroup of $\mathrm{GL}_n(\mathcal{O}_w)$ (`iwahori`, not unfolded). Let $I = U \cap b I_0 b^{-1}$, $I' = U' \cap I_0$ and $K = U \cap \mathrm{GL}_n(\mathcal{O}_w)$.

**Theorem.** There is $\beta \in (\mathbb{C}^\times)^m$ such that:

1. $\beta$ comes from $\alpha$ by a permutation and by inverting some entries;
2. $|\beta_1| \ge |\beta_2| \ge \dots \ge |\beta_m| \ge 1$;
3. there is a nonzero $y \in \sigma^I$ such that, for each cone point $l$,
$$\frac{1}{[K : I]} \sum_{g \in U/I} \mathbf{1}_{I b t_l b^{-1} I}(g)\, \sigma(g) y = \frac{1}{[K : I]}\, q^{\sum_{i} (n + 1 - 2i) l_i} \prod_{i} \beta_i^{l_i}\; y.$$

The left side is `levOp`. The Lean code writes $\sqrt{N w}$ for $q$ (`dlt`).

## Proof

The proof is `eigInertOf absEig heckeSum indexU`. The three lemmas are:

- `absEig` (`AbsEig`): the same statement on $U'$ with $I'$, for each diagonal $t \in U'$ whose diagonal valuations strictly decrease. The operator is the $T$ of `IsHeckeOpG`. The eigenvalue is $\chi_\beta(t) = \prod_i \beta_i^{a_i} q^{-(n+1-2i) a_i}$, with $a_i$ the valuation of $t_{ii}$ (`chiDeltaU`). We have not read its proof.
- `heckeSum` (`HeckeSum`): for compact open $J \le K$, the average of the characteristic function of $J t J$ equals $[K : J]^{-1}\, [J : J \cap t J t^{-1}]\, T$.
- `indexU` (`IndexU`): for a cone point $l$, $[I' : I' \cap t_l I' t_l^{-1}] = q^{2 \sum_i (n+1-2i) l_i}$.

The proof `eigInertOf` moves $\sigma$ and its Iwahori fixed vectors to $U'$ by conjugation with $b$. It applies `absEig` to get $\beta$ and $y$, takes the operator $T$ of $b t_l b^{-1}$ from `hecke_character_exists_unique`, and computes with `heckeSum` and `indexU`. The lemma `chi_eq` computes $\chi_\beta(t_l)$. The rest is bookkeeping.

## In the Lean code

The theorem is in [EigInert.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/InertEigenvalues/EigInert.lean#L8). The four statements are in [EigInert.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/EigInert.lean#L15), one folder up. The proof is `eigInertOf` in [AdmissibleTransport.lean](lean:Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/UniformizerValuations/InertEigenvalues/AdmissibleTransport.lean#L304).

Two hypotheses are not used. `eigInertOf` binds `IsUnifAt ϖ` as `_`. Of `IsWitt n w b`, only $b \in \mathrm{GL}_n(\mathcal{O}_w)$ is used, not $b^* b = J$. The cone condition is stronger than the strict dominance that `absEig` asks for.
