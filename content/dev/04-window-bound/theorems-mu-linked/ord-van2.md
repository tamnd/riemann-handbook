---
id: ord-van2
title: Ordinary adjoint cocycles at an automorphic point are coboundaries
kind: theorem
decl: UpperTheory.V.Th.ordVan2
module: Development.AutomorphicArithmetic.AutomorphicVarieties.TheoremsMuLinked.GaloisRepresentationTypes.OrdVan
covers: 516
status: drafted
drafted_by: writer@claude
---
This theorem proves $\mathrm{OrdVan2}$ from the hypothesis package $\mathrm{HypothesesH}$. It says that an ordinary polarized cocycle of the adjoint of an automorphic [[Galois representation|JQEYEQJY2G]] $\rho$ is a coboundary. The theorem [`Th.core`](/entry/th-core/) passes it to `core_of`, which turns it into the statement $\mathrm{Core}$ of the [main fork](/proof/vwin/). The proof turns $z$ into a derivation of the universal ring and kills it with a Hecke ideal $J$ from [`hidaX`](/entry/hida-x/) and the lemma `coreO`.

## Statement

Let $s$ be a Hida setting over a CM field $L$, with an odd prime $l$ and an auxiliary place $v_0$. Let $V$ be a level with set of places $S' = S$, and let $G_0 = \ker \eta$ be the Galois group of its frame. Let $r$ be a residual datum in dimension $n$ over the coefficient ring $\mathcal{O}$, and let $B$ be its universal ordinary determinant ring. Let $x \colon B \to \overline{\mathbb{Q}}_l$ be a point and let $\rho \colon G_0 \to \mathrm{GL}_n(\overline{\mathbb{Q}}_l)$ with polarization $P$. Suppose that:

1. $2 \le n \le 4$, and $r$ satisfies the conditions at $v_0$ (`V0ok`);
2. $x$ is arithmetic of weight $h$, and the determinant of $x$ is the determinant of $\rho$;
3. $\rho$ is continuous, its pull-back to $\Gamma$ is attached to a cuspidal, regular algebraic, conjugate self-dual representation (`IsAutCsd`), and the values $\rho(g)$ span $M_n(\overline{\mathbb{Q}}_l)$;
4. $\rho(g)^{T} P \rho(cgc^{-1}) = \varepsilon(g)^{1-n} P$, and $\rho$ is trivial on the inertia group $I_0$ at $v_0$;
5. $\psi_{v,i} \ne \psi_{v,j} \cdot \bar\varepsilon$ on the decomposition group at $v$, for all $v \mid l$ and all $i, j$, with $\bar\varepsilon$ the [[cyclotomic character|XSGB5K2KEG]];
6. `RegDet`: there are elements $\sigma_1, \dots, \sigma_q$ in the kernel of $\varepsilon$ with separable characteristic polynomials of $\rho(\sigma_j)$, and `DetQ` holds for them.

**Theorem.** Under $\mathrm{HypothesesH}$, let $z$ be an ordinary cocycle (`IsOrdCoc`): continuous, $z(gg') = z(g) + \rho(g) z(g') \rho(g)^{-1}$, polarized, zero on the inertia groups $I_u$ of $r$, and at each $v \mid l$ upper triangular up to a coboundary, with zero diagonal on inertia. Then there is a matrix $Y$ with $z(g) = \rho(g) Y \rho(g)^{-1} - Y$ for all $g$.

## Proof

1. Build the cohomology package $\mathrm{CohP}$ from `hP.litN.coh`. Check that the character $\varepsilon$ of the frame is $\bar\varepsilon$ on each decomposition group.
2. The private lemma `nmAbs` makes an integral model of $\rho$ and of $z$. It gives a new coefficient ring, residual datum $r'$ and ring $B'$, a point $x'$ of $B'$ and an $\mathcal{O}$-derivation $\delta$ at $x'$. The derivation kills the inertia characters. If $\delta$ kills all traces, then $z$ is a coboundary, through `trZero`. It takes `regArith` and `b0Ex (phiAll hC)` as inputs.
3. `lamEx` gives a level datum $\Lambda'$. Then `hidaX` gives an ideal $J$ of $B'$ with the property `PT` and with `LevelX`.
4. The flags in `hz.ord` and hypothesis 5 give the inputs of `PT` at $x'$. Thus $J \subseteq \ker x'$.
5. `coreO`, with `LevelX`, $J \subseteq \ker x'$ and `DetQ`, shows that $\delta$ kills all traces. Step 2 then ends the proof.

## In the Lean code

The theorem is in [OrdVan.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/GaloisRepresentationTypes/OrdVan.lean#L183). $\mathrm{OrdVan2}$ is in [OrdVan2.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdVan2.lean#L10), and `IsOrdCoc` is in [OrdinaryHeckeAlgebraIntegral.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/TheoremsMuLinked/OrdinaryHeckeAlgebraIntegral.lean#L159). The private lemma `nmAbs` is at line 136. We have not unfolded it past its conclusion.

Hypothesis 5 is for all $i, j$, also $i = j$: `nmAbs` uses only $i < j$, but `PT` needs all pairs. OrdinaryHeckeAlgebraIntegral.lean has a sibling statement `OrdVan` at line 230, with $1 \le n$ and only $i < j$. The lemma `coreO` (in MapOfRep.lean, line 142) proves `CoreO`, the statement that [this entry](/entry/core-o-of-literal-automorphy-n/) proves with `LevelIdealCondition` in place of `LevelX`.
