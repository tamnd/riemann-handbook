---
id: arith-intersection-system-of-poincare-lelong-res-k
title: An arithmetic intersection system, from Poincaré-Lelong and resolution
kind: theorem
decl: GlobalTheory.CompanionTheory.Ar.Pub.arithIntersectionSystem_of_poincareLelong_resK
module: Development.AutomorphicSpectrum.Proofs.MetricProofs.ArithIntersectionSystemOfPoincareLelong
covers: 327
status: drafted
drafted_by: writer@claude
---
This theorem builds arithmetic intersection numbers on arithmetic varieties in products of projective spaces, with projection rules. It assumes an arithmetic Poincaré-Lelong formula and resolution of singularities in characteristic $0$. It has two users below the [literature step](/step/every-character-of-literature/). `PositivityTheory.HtPt.Ah.ais` supplies both hypotheses from literature inputs. The second name `GlobalTheory.T.arith_intersection_system_of_poincare_lelong` feeds [the arithmetic intersection calculus from Poincaré-Lelong and resolution](/entry/ar-calc-direct/).

## Statement

The words *arithmetic variety*, *metrized line bundle* and *family of heights* are as in [the projection formula, in two forms](/entry/gen-deg-and-pf-coord/).

**Hypotheses.**

- `PoincareLelong`: the formula `ArithmeticPoincareLelongFormula`. Let $X$ have dimension $n + 2$, let $L_1, \dots, L_n, A$ be smooth metrized line bundles, let $B$ be a smooth metric of degree $0$, and let $s \notin X$ be a form of the degree of $A$. Then the integral of $\log \|s\|_A$ against $\log B$ and the $L_j$ on $X(\mathbb{C})$ equals the sum, over the horizontal components $W$ of $\operatorname{div}(s)$ with multiplicity, of the integral of $\log B$ on $W(\mathbb{C})$, minus the integral of $\log B$ against $\log h_A$ and the $L_j$ on $X(\mathbb{C})$. This is an integrated form of the Poincaré-Lelong formula $dd^c \log \|s\|^2 = \delta_{\operatorname{div}(s)} - c_1(A)$. We have not unfolded the density of the integrals.
- `ResKStatement`: let $k$ be a field of characteristic $0$ and $X \subseteq \mathbb{P}^M_k$ a reduced closed subscheme, with a dense open $U$ that is smooth of dimension $D$. Then there is a closed subscheme $X' \subseteq \mathbb{P}^M_k \times \mathbb{P}^r_k$, smooth of dimension $D$, whose projection $f \colon X' \to X$ is an isomorphism over $U$, with $f^{-1}(U)$ dense and $X' \setminus f^{-1}(U)$ a divisor with simple normal crossings in local coordinates. This is resolution of singularities in the sense of Hironaka (Ann. of Math. 79, 1964).

**Theorem.** Under these hypotheses there is a system $I$ of arithmetic intersection numbers $I(X; L_1, \dots, L_d)$, such that:

1. $I$ satisfies the axioms `IsFamily` of [the existence theorem](/entry/thm-iexists/);
2. $I$ is additive in each bundle (`IsMultilinFam`);
3. the projection formula `HasPFCoord` holds, with the degree of the extension of function fields;
4. `HasContractMixed`: if $\pi$ forgets some blocks, $\dim X' = d + r$ and $\dim \pi(X') < d$, then $I(X'; \pi^* L_1, \dots, \pi^* L_d, N_1, \dots, N_r) = 0$.

## Proof

The proof is one call to `ArithIntersectionSystem.of_found` with three inputs.

- `resolution_exists_of_resolution_statement` turns `ResKStatement` into the analytic form `ResExistsStatement`.
- [The arithmetic intersection numbers exist](/entry/intersection-exists-of-poincare-lelong/) takes `PoincareLelong` and that analytic form, and gives a family $I$ with (1).
- [The projection formula from resolution](/entry/degree-and-coordinates-of-resolution/) gives (3). The proof uses only its second half.
- `contractMixed_closed`, in the same file, proves (4) with no hypotheses.

`of_found` then gets (2) from (1) by `multilin_of_isFamily`: symmetry moves any slot to the last one.

## In the Lean code

The theorem is in [ArithIntersectionSystemOfPoincareLelong.lean](lean:Development/AutomorphicSpectrum/Proofs/MetricProofs/ArithIntersectionSystemOfPoincareLelong.lean#L42), with `contractMixed_closed` at line 30. `PoincareLelong` is in [PoincareLelong.lean](lean:Development/AutomorphicSpectrum/PublishedTheorems/Metrics₂/PoincareLelong.lean#L6) and unfolds to [InterSt.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/InterSt.lean#L76). `ResKStatement` is in [BlowupProjStatement.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/BlowupProjections/BlowupProjStatement.lean#L66).

`PoincareLelong` is used only by the existence of $I$.
