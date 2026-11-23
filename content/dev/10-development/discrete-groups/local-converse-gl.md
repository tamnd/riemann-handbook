---
id: local-converse-gl
title: A local converse theorem for cuspidal representations of GL(n)
kind: theorem
decl: DiscreteGroups.sglob.LConv.localConverseGL
module: Development.DiscreteGroups.GlobalIrreducibility.LConvFinal
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem proves the statement `LocalConverseGL`: two cuspidal representations of $\mathrm{GL}_{m+1}$ over a $p$-adic field with the same epsilon values against every irreducible representation of $\mathrm{GL}_m$ are isomorphic. It is one of the published statements that the proof needs below [EveryCharacter from Row0b](/step/every-character-of-row/), and the code proves it instead of assuming it. The proof is an assembly of twelve proved parts.

## Statement

Let $k$ be a non-archimedean local field of characteristic $0$, let $\psi$ be a nontrivial continuous additive character of $k$, and let $m \ge 1$. Let $N_m$ be the upper unipotent subgroup of $\mathrm{GL}_m(k)$, $\iota(g) = \operatorname{diag}(g, 1)$ and $\tilde g = w_0\, {}^t g^{-1}$ with $w_0$ the long Weyl element. A *test function* on $\mathrm{GL}_m(k)$ is locally constant, left $N_m$-invariant and compactly supported modulo $N_m$. A linear functional $I$ on functions on $\mathrm{GL}_m(k)$ is *invariant* if $I(f(\cdot\, x)) = I(f)$ for each test function $f$ and each $x$.

Let $\pi$ be a representation of $\mathrm{GL}_{m+1}(k)$, $\tau$ one of $\mathrm{GL}_m(k)$ with central character $\omega$, and $e \in \mathbb{C}$. Say that $(\pi, \tau)$ *has epsilon value* $e$ (`HasPairEps`) if for each $\psi$-Whittaker functional $\lambda$ on $\pi$, each $\psi^{-1}$-Whittaker functional $\lambda'$ on $\tau$, each invariant $I$ and all $v, v'$,

$$I\big(g \mapsto \lambda(\pi(\widetilde{\iota(g)})v)\, \lambda'(\tau(\tilde g)v')\big) = \omega(-1)^m\, e\, I\big(g \mapsto \lambda(\pi(\iota(g))v)\, \lambda'(\tau(g)v')\big).$$

This is the functional equation of the zeta integrals of Jacquet, Piatetski-Shapiro and Shalika with no complex variable $s$.

**Theorem.** Let $\pi_1, \pi_2$ be irreducible smooth cuspidal representations of $\mathrm{GL}_{m+1}(k)$. Suppose that for each irreducible smooth $\tau$ of $\mathrm{GL}_m(k)$ there is one $e$ such that $(\pi_1, \tau)$ and $(\pi_2, \tau)$ both have epsilon value $e$. Then $\pi_1 \cong \pi_2$.

## Proof

The proof is `localConverseGL_of_leaves` applied to twelve proved statements. The last one, `glue`, does the following.

1. Cuspidal representations are generic (`cuspGen`). This gives Whittaker functionals $\lambda_1, \lambda_2$.
2. `bigCell`: if each pair $v_1, v_2$ whose Whittaker functions agree on $\iota(\mathrm{GL}_m(k))$ also has equal values at $w_0$, and one such pair has $\lambda_1(v_1) \ne 0$, then $\pi_1 \cong \pi_2$. The pair with $\lambda_1(v_1) \neq 0$ comes from `kirBump`.
3. For the condition at $w_0$, the difference of the two Whittaker functions at $\widetilde{\iota(g)}$ is a test function. The hypothesis, applied to the twist of each $\tau$ by $g \mapsto \tilde g$, shows that it pairs to $0$ with the Whittaker functions of every irreducible $\tau$. By `WhitSep` it is $0$. Evaluate at $g = 1$.

`WhitSep` (completeness of Whittaker functions of irreducibles) is the deep part. It comes from extreme invariant forms (`sepOfExtreme`, `extremeExists`, `extremeIrred`) and from admissibility of unitary representations (`unitOfUnif`, `altIdentity`, `finiteOfAlt`), which rests on a uniform bound for commuting matrices (`commBound`, `unifOfComm`).

## In the Lean code

The theorem is at [LConvFinal.lean](lean:Development/DiscreteGroups/GlobalIrreducibility/LConvFinal.lean#L18). The statement is in [LocalConverseGL.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/LocalConverseGL.lean#L12), `HasPairEps` in [HasExponentZeroIff.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasExponentZeroIff.lean#L100), the twelve parts and `localConverseGL_of_leaves` in [LConvCut.lean](lean:Development/DiscreteGroups/GlobalIrreducibility/LConvCut.lean#L115), and `glue` in [LConvGlue.lean](lean:Development/DiscreteGroups/GlobalIrreducibility/LConvGlue.lean#L148).

The statement is close to the local converse theorem of Henniart (Invent. Math. 113 (1993), 339 to 350), but the forms differ. The Lean form twists only by $\mathrm{GL}_m$, asks for cuspidal $\pi_i$, uses one point of the functional equation, and needs characteristic $0$ (only `WhitSep` uses it). Since $\tau$ runs over all irreducible representations, the twists $\tau \otimes |\det|^s$ play the role of $s$. For a non-generic $\tau$ the condition holds for every $e$.

The theorem is used by `local_converse_gl_of_literature` and `local_converse_gl_of_open`. The first ignores its argument; the [literature chapter](/proof/literature/) explains this pattern.
