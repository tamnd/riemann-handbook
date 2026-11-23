---
id: exists-fj-ne-zero-at-split-point-prime
title: A cusp form with a nonzero low Fourier-Jacobi coefficient has one at a split point
kind: theorem
decl: GlobalTheory.FJDetect.exists_fj_ne_zero_at_split_point'
module: Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.ExistsFjNeZeroAtSplitPoint
covers: 649
status: drafted
drafted_by: writer@claude
---
This theorem says that if a low Fourier-Jacobi coefficient of a cusp form is nonzero at some point, then it is nonzero at a good point. At a good point the vectors orthogonal to $\xi$ split by sign with bounded norms, and an integrality condition holds. Its only user is [the split point with fixed bounds](/entry/exists-split/), which fixes the constants.

## Statement

Let $X$ be lattice data (`DataX`) of rank $r$: a CM field $E$ with CM type $\Psi$, a hermitian form $h$ of signature $(p_0, r - p_0)$ at each $\tau \in \Psi$, a lattice $\Lambda$ with dual lattice $L'$, a level $g$, a group $\Gamma$ and characters $\chi_\lambda$ of $\Gamma$. A frame is a family of complex $r \times r$ matrices indexed by $\Psi$. The domain is the set of invertible frames whose leading Gram minors have the right signs. A section of weight $\lambda$ is a holomorphic function on the domain that transforms by $\lambda$ under upper triangular matrices and by $\chi_\lambda$ under $\Gamma$.

For an isotropic $\xi \in \Lambda$ and $\nu \colon \Psi \to \mathbb{R}$, $\mathrm{fj}_{\lambda,\xi,\nu}(P)$ is the average of $P$ along the flow in the direction of $\xi$ against $e^{-4\pi i \sum_\tau \nu_\tau s}$, over a fundamental domain of the periods. $\mathrm{SS}(\lambda)$ is the set of bounded sections with $\mathrm{fj}_{\lambda,\xi,0} = 0$ for all $\xi$. $\mathrm{SS}_{>c}(\lambda)$ is the subset with $\mathrm{fj}_{\lambda,\xi,\nu} = 0$ whenever $\sum_\tau \nu_\tau \le c$.

**Theorem.** Let $\lambda$ be dominant, $c_1 > 0$, $w \ge 1$, $r \le w$ and $\sum_\tau \mathrm{spread}(\lambda,\tau) \le w$. Suppose that $\chi_\lambda(\gamma) = 1$ for each $\gamma \in \Gamma$ with $\gamma v - v \in g\Lambda$ for all $v \in \Lambda$. Let $P \in \mathrm{SS}(\lambda)$ with $P \notin \mathrm{SS}_{>c_1}(\lambda)$. Then there are an isotropic $\xi$ and $\nu \ge 0$ with $\sum_\tau \nu_\tau \le c_1$ such that `ShortVectorHypotheses` holds at some frame $z_0$, and for each integer $n' \ge 1000\, m_s / r_h$ there are a point $x$ of the domain and $v_1, \dots, v_{r-2} \in L'$ with:

1. each $v_j$ orthogonal to $\xi$, and $\xi, v_1, \dots, v_{r-2}$ linearly independent over $E$;
2. the first $p_0 - 1$ of the $v_j$ positive at every $\tau$, the rest negative, the two groups orthogonal, and the operator `Jz` at $x$ acting by $i$ and $-i$ on their images;
3. $|\tau\, h(v_j, v_j)| \le L_a^2$;
4. for each $\mu \in \Lambda_p(\xi)$, $n' \cdot \mathrm{aproj}_x(\xi, \mu) = e\xi$ for some $e \in E$ with $e\xi \in \Lambda$;
5. $\mathrm{fj}_{\lambda,\xi,\nu}(P)(x) \neq 0$.

The constants $r_h$, $L_a$, $m_s$ are explicit (`d6rh`, `d6La`, `frameIndexBound`). Clauses 1 to 3 are `SplitData`.

## Proof

1. Since $P \notin \mathrm{SS}_{>c_1}$, there are $\xi$, $\nu$ with $\sum \nu_\tau \le c_1$ and $x$ with $\mathrm{fj}(P)(x) \neq 0$.
2. `sign_of_bdd` with `moderateCoefficientPositivity_holds` gives $\nu \ge 0$.
3. A private lemma gives $z_0$ in `FramesOverBasis ξ` where $\widehat N$ is more than half its supremum over that set. It moves $x$ into that set along the imaginary flow. There $s \mapsto \mathrm{fj}(P)(\mathrm{flow}_s x)\, e^{-4\pi i \sum \nu_\tau s}$ is holomorphic and invariant under real translations, so it does not change. The supremum is finite by `fj_bound`.
4. This gives `ShortVectorHypotheses`. `FundamentalDomainPointBound`, proved by `fd_point_assembly` from nine library theorems, gives the rest.

## In the Lean code

The theorem is in [ExistsFjNeZeroAtSplitPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs/ExistsFjNeZeroAtSplitPoint.lean#L189). `fd_point_assembly` is in [FdPointAssembly.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/FundamentalDomains/FundamentalDomainExtension/PointAssembly/FdPointAssembly.lean#L6).

- `fd_point_assembly` takes nine hypotheses but does not use three of them: `ShortVectorBound`, `IsotropicCoefficientSplitting` and `NoShortVectorLowerBound`. They are still used inside two of its other inputs.
- The name ends in a prime. There is no theorem without the prime.
- We have not unfolded `Λp`, `aproj`, `hatN` or the nine inputs.
