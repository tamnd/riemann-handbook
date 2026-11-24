---
title: Ranks of cusp forms at shifted weights
decls:
  - GlobalTheory.T.twoLevelFlagDomain_cuspForm_ranks_shifted_weights
  - GlobalTheory.ShareRanks.ranks
  - GlobalTheory.ShareRanks.compT
  - GlobalTheory.ShareRanks.compX
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ranks of cusp forms at shifted weights

This section compares the dimensions of the spaces of cusp forms on a two level datum at three weights: a weight $\kappa$, the weight $\kappa - \nabla(s)$ and the weight $\kappa + 2\nabla(s)$. The result is used by [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). Multiplication by a cusp form of weight $\nabla(s)$ that is nonzero somewhere gives the comparisons. Such a form exists on each component by [the independent translates theorem](/entry/independent-translates/) of section 11.

We keep the notation of section 11: the two level datum with the finite group $U$ acting on the finite set $C$, the data $X_c$ of rank $r$ over $E$, the domain, the cusp forms $SS(\lambda)$ and the determinant weight $\nabla(s)$. Put

$$\begin{aligned} \dim X &= |\Psi|\, p_0 (r - p_0), \\ n &= |\Psi|\, r (r - 1)/2, \\ s_0 &= 2r + 50 r^2 \dim X + 2. \end{aligned}$$

Here $n$ is the complex dimension of the flag variety of each component, and $s_0$ is even. For a weight $\lambda$ let $\mathrm{cusp}(\lambda)$ be the complex span of the restrictions to $C \times$ domain of the cusp forms of weight $\lambda$ on the datum. Each element is a family of functions, one on the domain of each component.

### Archimedean data

Let $X$ be one component. An *archimedean datum* for $X$ is a pair of weights $L$ and $F$ with an integer $T$, together with curvature margins and a *flat datum*. The flat datum consists of a section $w_0$ and sections $s_0, \ldots, s_{n-1}$ of weight $L$ with $\delta$ points of the domain, such that the common zeros of the $s_q$ are exactly the orbits of these points and the coordinate Jacobian of $s/w_0$ is nonzero there. It gives $2 \leq n$ and $11 n^2 \leq T$. The number $\delta$ is the *degree* of the flat datum.

The two level datum *has archimedean data* at a weight $\kappa$ and an integer $T$ if there are weights $L$ and $F$ with $\kappa = F + T L$ such that the following hold:

1. the gaps of $L$ inside each block of the signature are at least $1$, and the pairing of $L$ across the blocks is at least $1.9\, T$;
2. the gaps of $F - k_{\log} - (n + 2) L$ inside each block are at least $0$, and its pairing across the blocks is at least $1$, where $k_{\log}$ is the canonical weight;
3. each component $X_c$ has an archimedean datum with the weights $L$ and $F$ and the integer $T$.

**Lemma 7.14.1 (Ranks on one component).** Let $X$ be a component with $0 < p_0 < r$ and an archimedean datum $(L, F, T)$ with flat datum of degree $\delta$, which satisfies conditions 1 and 2. Let $s \leq T$ be even, and let $u \in SS(\nabla(s))$ be nonzero at some frame of the domain. Then the following hold.

1. Every linearly independent family in $SS(F + T L)$ has at most $\delta \binom{T + 2n + 6}{n}$ members.
2. Every linearly independent family in $SS(F + T L - \nabla(s))$ has at most $\delta \binom{T + 2n + 6}{n}$ members.
3. Every linearly independent family in $SS(F + T L + 2 \nabla(s))$ has at most $\delta \binom{T + 3n + 10}{n}$ members.
4. There is a linearly independent family of $\delta \binom{T + n}{n}$ members in $SS(F + T L - \nabla(s))$.

Lean: `GlobalTheory.ShareRanks.compX` (also `GlobalTheory.ShareRanks.compT`).

*Proof.* We take the claims in order.

1. This is the upper bound for the model of a flat datum: an independent family of bounded sections of weight $F + T L$ has at most $\delta \binom{T + 2n + 6}{n}$ members.
2. Let $(f_q)$ be independent in $SS(F + T L - \nabla(s))$. The products $f_q u$ lie in $SS(F + T L)$, since the weights add and the product of cusp forms is a cusp form. They are independent. Indeed, if $\sum a_q f_q u = 0$ on the domain, then $\sum a_q f_q = 0$ on the open set where $u \neq 0$. This set is not empty, and the domain is connected, so $\sum a_q f_q = 0$ on the domain. Claim 1 gives the bound.
3. From $u$ the theorem on shifted weights gives a bounded section $w$ of weight $(n + 4) L - 2 \nabla(s)$ that is nonzero somewhere. Let $(f_q)$ be independent in $SS(F + T L + 2 \nabla(s))$. The products $f_q w$ are bounded sections of weight $F + (T + n + 4) L$, and they are independent as in claim 2. The upper bound for bounded sections at this weight gives at most $\delta \binom{(T + n + 4) + 2n + 6}{n} = \delta \binom{T + 3n + 10}{n}$ members.
4. This is the lower bound for the rank of cusp forms at a determinant weight on one component. It uses $u$, the margins and conditions 1 and 2.

The cast form of the lemma reads the same statements for weights given on a fixed CM type, with the bounds $2 \leq n$ and $11 n^2 \leq T$ of the archimedean datum. $\square$

### The ranks

**Theorem 7.14.2 (Ranks at shifted weights).** Let a two level datum of rank $r$ over $E$ satisfy the level hypothesis for the trivial subgroup of $U$, with $0 < p_0 < r$. Let $\kappa$ be a weight and $T$ an integer such that the datum has archimedean data at $\kappa$ and $T$, and $s_0 \leq T$. Put $\varepsilon = n(n + 6)/T$. Then the spaces $\mathrm{cusp}(\kappa)$, $\mathrm{cusp}(\kappa - \nabla(s_0))$ and $\mathrm{cusp}(\kappa + 2\nabla(s_0))$ are finite dimensional, and

$$\begin{aligned} (1 - \varepsilon) \dim \mathrm{cusp}(\kappa) &\leq \dim \mathrm{cusp}(\kappa - \nabla(s_0)), \\ \dim \mathrm{cusp}(\kappa + 2\nabla(s_0)) &\leq 2 \dim \mathrm{cusp}(\kappa - \nabla(s_0)). \end{aligned}$$

Lean: `GlobalTheory.T.twoLevelFlagDomain_cuspForm_ranks_shifted_weights` (also `GlobalTheory.ShareRanks.ranks`).

*Proof.* We take the steps in order.

1. Restrict the group action to the trivial subgroup. The level hypothesis holds for this datum. The number $s_0$ is even and $s_0 \geq 2r + 50 r^2 \dim X + 1$. So [the independent translates theorem](/entry/independent-translates/) gives $u_0$ of weight $\nabla(s_0)$, with each component a cusp form, such that for each $c$ some frame $x$ has a nonzero determinant of translates.
2. For the trivial group the matrix of translates has the single entry $u_0(c, \mathrm{tr}(1, c) x)$. So this value is not zero. The cocycle rule at $u = v = 1$ gives $\mathrm{tr}(1, c) \in \Gamma_c$. Since $\chi = 1$ on $\Gamma_c$, we get $u_0(c, x) \neq 0$. So each component $u_{0, c}$ is nonzero at a frame of the domain.
3. Fix $c$. The dimension of the flag variety of $X_c$ is $n$. [The ranks on one component](/entry/comp-x/), applied with $u = u_{0, c}$, $s = s_0 \leq T$ and the archimedean datum of $X_c$, give a degree $\delta_c$ with the four claims, and $2 \leq n$, $11 n^2 \leq T$.
4. An independent family in $\mathrm{cusp}(\lambda)$ restricts on each component to a family in the span of $SS(\lambda)$ of $X_c$. So the upper bounds on the components give that $\mathrm{cusp}(\lambda)$ is finite dimensional, with

$$\dim \mathrm{cusp}(\lambda) \leq \sum_{c} N_c,$$

for $N_c = \delta_c \binom{T + 2n + 6}{n}$ at $\lambda = \kappa$ and at $\lambda = \kappa - \nabla(s_0)$, and for $N_c = \delta_c \binom{T + 3n + 10}{n}$ at $\lambda = \kappa + 2\nabla(s_0)$.
5. A family of forms on one component, extended by zero to the other components, is a family of cusp forms on the datum. So the lower bound on the components gives

$$\sum_{c} \delta_c \binom{T + n}{n} \leq \dim \mathrm{cusp}(\kappa - \nabla(s_0)).$$

6. For $n \geq 2$ and $11 n^2 \leq T$ the two binomial bounds

$$\begin{aligned} \binom{T + 3n + 10}{n} &\leq 2 \binom{T + n}{n}, \\ \Bigl(1 - \frac{n(n + 6)}{T}\Bigr) \binom{T + 2n + 6}{n} &\leq \binom{T + n}{n} \end{aligned}$$

hold. Combine them with steps 4 and 5. If $1 - \varepsilon < 0$, the first inequality of the theorem is clear. Otherwise $(1 - \varepsilon) \dim \mathrm{cusp}(\kappa) \leq \sum_c \delta_c (1 - \varepsilon) \binom{T + 2n + 6}{n} \leq \sum_c \delta_c \binom{T + n}{n}$. The second inequality is $\sum_c \delta_c \binom{T + 3n + 10}{n} \leq 2 \sum_c \delta_c \binom{T + n}{n}$.

This proves the theorem. $\square$

The theorem uses the independent translates theorem only for the trivial group. In that case the statement is that each component carries a cusp form of weight $\nabla(s_0)$ that is not identically zero. The full group $U$ plays no role in this proof.

**Remark 7.14.3 (Formalization).** The statement `T.twoLevelFlagDomain_cuspForm_ranks_shifted_weights` is a `first | exact` wrapper under `maxHeartbeats 1000000`. The proof `ranks` is at line 289 of [TwoLevelFlagDomainCuspFormRanksShiftedWeights.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/TwoLevelFlagDomainCuspFormRanksShiftedWeights.lean#L289). It applies the independent translates statement to `sub M ⊥`, the datum restricted to the trivial subgroup, and uses `exists_pull_ne` at line 208, `tr_one_mem` at line 221 and `nzT` at line 235 for step 2. The per component bounds are `compX` at line 154 and its cast form `compT` at line 186, with `nd_comp` at line 229. The sums over components are `upper_cusp` at line 249 and `lower_cusp` at line 262, built on `span_upper` at line 47 and `lower_of_comps` at line 110; the independence of products is `indep_mul` at line 132. The goal `Ranks`, the condition `ArchOn` and the number `sOf` are at lines 38, 47 and 52 of [ExistsArchOne.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ExistsArchOne.lean#L38). The number `sOf` adds $2$ and not $1$, which makes it even without a parity case.
