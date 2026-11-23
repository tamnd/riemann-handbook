---
id: slope-bound-and-lemma-s-of-siegel
title: The slope bound for semi-abelian Lie bundles from the Siegel lemma
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Sl.slopeBound_and_lemmaS_of_siegel
module: Development.AutomorphicSpectrum.Proofs.GeometryProofs.SlopeBoundOfLineLargeDegree
covers: 1157
status: drafted
drafted_by: writer@claude
---
This theorem bounds the maximal slope of the Lie bundle of a semi-abelian scheme with a principal polarization by a constant times the logarithm of its rank and its height. Its one hypothesis is a Siegel lemma for hermitian lattices. Its proof is one line that composes three other lemmas, and the work is in them. It goes through the renaming [`T.slope_bound_of_line_large_degree`](/entry/slope-bound-of-line-large-degree/) to [`given_of_inputs`](/entry/given-of-inputs/), where it gives part 9 of `Top.Given`. The hypothesis comes from [`lineOfLargeDegree_of_use`](/entry/line-of-large-degree-of-use/).

## Statement

**Hypothesis** (`LineOfLargeDegree.Statement`). For each number field $K$, each hermitian lattice $F$ of rank $i \ge 1$ over $K$ and each $\varepsilon > 0$, there are a finite extension $K'/K$ and $v \ne 0$ in $K'^{\,i}$ with $\mu(F) - \frac12 \log i - \varepsilon \le \widehat{\deg}_F(v)$. The written proof calls this an absolute Siegel lemma.

**Conclusion** (`SlopeBoundSt`). There is $C \ge 0$ with the following property. Let $E$ be a CM field with a host $H$, and $L$ a number field. Let $t$ be a semi-abelian scheme over $\mathcal{O}_L$ whose generic fibre is principal (`IsPrincipal`: the conditions `IsProper`, `Out.RelAmple` and `Out.KTriv`, which we have not unfolded). Let $\overline{B}$ be a hermitian bundle over $\mathcal{O}_L$ with a Lie model that is the fibre of the Hodge inner product. Then
$$\mu_{\max}(\overline{B}) \le C \log\bigl(2 + \operatorname{rk} B + \max(-\widehat{\deg}_n \overline{B}, 0)\bigr).$$
Here $\mu_{\max}$ is the supremum of $\widehat{\deg}_n(F)/\operatorname{rk} F$ over the nonzero subbundles $F$, and $\widehat{\deg}_n = \widehat{\deg}/[L:\mathbb{Q}]$. The conclusion also states `Prov.LemmaS`, which is an abbreviation for `SlopeBoundSt`.

## Proof

The proof is `slope_bound_of_large_degree_line hS (key_degree_of_bad_reduction key_bad_reduction_holds)`.

1. `key_bad_reduction_holds` proves `KeyBadSt`. For a rule $\kappa$ with five properties (`Homog`, `Funct`, `UnitSp`, `ThetaOne`, `ArchNorm`), a discrete valuation ring $R$ with finite residue field and fraction field $K$ of characteristic $0$, and a semi-abelian $t$ over $R$ with a theta section that no nonunit divides, the value of $\kappa$ is integral. We have not unfolded the rule.
2. `key_degree_of_bad_reduction` turns this into `KeyDegSt`: after a finite extension, there is a theta section whose theta mean-square norms have mean logarithm at most $\frac12 h + C g$, with $g = \operatorname{rk} B \ge 1$ and $h = \max(-\widehat{\deg}_n \overline{B}, 0)$.
3. `slope_bound_of_large_degree_line` is a renaming of `TopSlope.slopeBound`. That proof gets from `line_of_key_degree` a constant $C$ with $-\operatorname{mean}_\sigma \log |x|_\sigma \le C \log(2 + g + h)$ for each $x \ne 0$ in $B$. For a subbundle $F \ne 0$, `short_vector_of_submodule` gives $x$ over an extension $L'$ with $\mu(F) - \frac12 \log \operatorname{rk} B - 1 \le -\operatorname{mean} \log |x|$. An isometric base change moves $x$ into the Lie bundle over $L'$. With $\ell = \log(2 + g + h) \ge \frac23$ and $\log \operatorname{rk} B = \log g \le \ell$, this gives $\mu(F) \le (C + 2)\ell$.

We have not opened the proofs of `line_of_key_degree` and `keyDeg_of_keyBad`.

## In the Lean code

The theorem is in [SlopeBoundOfLineLargeDegree.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLineLargeDegree.lean#L17). The three lemmas are renamings: of `TopSlope.slopeBound` in [SlopeBoundOfLargeDegreeLine.lean](lean:Development/AutomorphicSpectrum/Proofs/GeometryProofs/SlopeBoundOfLargeDegreeLine.lean#L94), of `keyDeg_of_keyBad` and of `KP.key_bad`. `SlopeBoundSt` is in [SlopeBoundSt.lean](lean:Development/AutomorphicSpectrum/Definitions/GlobalGeometry/SlopeBoundSt.lean#L72).

The conjunction `SlopeBoundSt ∧ Prov.LemmaS` states one fact twice. `TopSlope.slopeBound` ends with `⟨hS, hS⟩`.
