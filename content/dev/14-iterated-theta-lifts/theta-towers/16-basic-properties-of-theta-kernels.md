---
title: Basic properties of theta kernels
decls:
  - GlobalTheory.ThKBasic.theta_kernel_basic_properties
  - GlobalTheory.T.theta_pair_moderate_growth
  - GlobalTheory.ThetaModGrowthPair.theta_moderate_growth
  - GlobalTheory.T.theta_pair_sum_rational
  - GlobalTheory.ThetaRatPair.theta_sum_omega_rational
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Basic properties of theta kernels

The theta integrals of the earlier sections integrate theta kernels over fundamental domains. For this to make sense, a theta kernel must be continuous, invariant under the rational points of both groups, and of moderate growth. This section proves these three properties for every dual pair of unitary groups over a CM extension, together with the continuity of the kernel in the archimedean Schwartz function. The tower of [Section 3.14.6](/entry/tower-alt-bis/) uses them through the convergence of its theta integrals.

Let $E/F$ be a CM extension of number fields with the nontrivial automorphism $\sigma$. Let $X$ be a Hermitian space of rank $n$ and $W$ a skew-Hermitian space of rank $d$ over $E$, with Gram matrices $J_X$ and $J_W$, and with signatures $(r, s)$ and $(r', s')$ at the real places. A pair is the data of a model of $X \otimes W$, characters $\chi_X$ and $\chi_W$ and a Weil representation $\omega$ of the adelic unitary groups $U(X) \times U(W)$ on the Schwartz space of the adelic points of $\mathrm{Mat}_{n \times d}(F)$ (as a module for the doubled space), with the usual conditions; we have not unfolded them all. Let $\mathcal S$ be the span of the pure tensors $f \otimes \varphi$ of an archimedean Schwartz function $f$ and a finite Schwartz function $\varphi$. For $\Phi \in \mathcal S$ the theta sum is

$$\Theta(\Phi) = \sum_{\xi \in \mathrm{Mat}_{n \times d}(F)} \Phi(\xi),$$

and the theta kernel is $\theta_\Phi(g, h) = \Theta(\omega(g, h)\Phi)$. Let $\mathrm{ht}(g)$ be the height of an adelic point $g$.

**Theorem 3.16.1 (Invariance of the theta sum).** For a pair, rational points $\gamma \in U(X)(F)$ and $\gamma' \in U(W)(F)$ and $\Phi \in \mathcal S$,

$$\Theta(\omega(\gamma, \gamma')\Phi) = \Theta(\Phi).$$

Lean: `GlobalTheory.ThetaRatPair.theta_sum_omega_rational` (also `GlobalTheory.T.theta_pair_sum_rational`, a second name).

*Proof.* Fix an infinite place $w$ of $F$. The signature of $X$ at $w$ shows that $J_X$ has a nonzero determinant after the embedding at $w$, so $\det J_X \neq 0$. For $W$ the same argument applies to $i J_W$, which is Hermitian, so $\det J_W \neq 0$. Then the rational points act through a rational Darboux decomposition of the symplectic space, and the Weil representation of a rational point of the symplectic group fixes the theta distribution. This is the invariance of A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), in the form proved in the formalization. $\square$

**Theorem 3.16.2 (Moderate growth).** For a pair and $\Phi \in \mathcal S$ there are a constant $C$ and an exponent $k$ such that for all $g$ and $h$,

$$|\theta_\Phi(g, h)| \le C\, \bigl(\mathrm{ht}(g)\, \mathrm{ht}(h)\bigr)^k.$$

Lean: `GlobalTheory.ThetaModGrowthPair.theta_moderate_growth` (also `GlobalTheory.T.theta_pair_moderate_growth`, a second name).

*Proof.* We use three bounds. First, a bound on lattice sums: there are $N_0$, $k_2$ and $C_2$ such that, if a function $\Psi$ is supported on the $(1/m)$-lattice at the finite places and is bounded by $B$ at the archimedean places in the right sense, then $|\Theta(\Psi)| \le C_2\, B\, m^{k_2}$. Second, a common denominator: there are $C_3$ and $k_3$ such that $\omega(g, h)\Phi$ is supported on the $(1/m)$-lattice for some $m \ge 1$ with

$$m \le C_3\, H^{k_3}, \qquad H = \mathrm{ht}(g)\, \mathrm{ht}(h).$$

Third, decay at the archimedean places: there are $C_1$ and $k_1$ such that $\omega(g, h)\Phi$ satisfies the archimedean bound with $B = C_1 H^{k_1}$. Insert the second and third bounds into the first:

$$\begin{aligned} |\theta_\Phi(g, h)| &\le C_2\, C_1 H^{k_1}\, m^{k_2} \\ &\le |C_2|\, |C_1|\, |C_3|^{k_2}\, H^{k_1 + k_3 k_2}. \end{aligned}$$

So $C = |C_2|\, |C_1|\, |C_3|^{k_2}$ and $k = k_1 + k_3 k_2$ work. $\square$

**Theorem 3.16.3 (Basic properties of theta kernels).** Assume the local inputs. For every pair and every $\Phi \in \mathcal S$:

1. the map $(g, h) \mapsto \theta_\Phi(g, h)$ is continuous on $U(X) \times U(W)$;
2. $\theta_\Phi(\gamma g, \gamma' h) = \theta_\Phi(g, h)$ for all rational points $\gamma$, $\gamma'$;
3. $\theta_\Phi$ has moderate growth as above.

Also, for every finite Schwartz function $\varphi$ and all $g$, $h$, the map $f \mapsto \theta_{f \otimes \varphi}(g, h)$ is continuous on the archimedean Schwartz space.

Lean: `GlobalTheory.ThKBasic.theta_kernel_basic_properties`.

*Proof.* The Weil representation of a pair is a unitary splitting: it preserves $\mathcal S$, it is continuous in a sense that we have not unfolded, and its action on a pure tensor is admissible. An admissible form $l$ on $\mathcal S$ agrees with the theta sum $\Theta$ on $\mathcal S$.

1. The splitting gives continuity of $(g, h) \mapsto l(\omega(g, h)\Phi)$, and this function is $\theta_\Phi$, since $\omega(g, h)\Phi \in \mathcal S$.
2. Since $\omega$ is a representation, $\omega(\gamma g, \gamma' h)\Phi = \omega(\gamma, \gamma')\, \omega(g, h)\Phi$. Apply [Theorem 3.16.1](/entry/theta-sum-omega-rational/) to $\omega(g, h)\Phi$, which lies in $\mathcal S$.
3. This is [Theorem 3.16.2](/entry/theta-moderate-growth/).

For the last claim, the admissibility of the splitting at $(g, h)$ gives a continuous linear map $T$ on the archimedean Schwartz space with $T(f) = l(\omega(g, h)(f \otimes \varphi))$, and this is $\theta_{f \otimes \varphi}(g, h)$. $\square$

**Remark 3.16.4 (Formalization).** All three theorems take the local inputs and none uses them: the invariance ([ThetaSumOmegaRational.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaSumOmegaRational.lean#L13)) and the moderate growth ([ThetaPairModerateGrowth.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaPairModerateGrowth.lean#L16)) drop the hypothesis at once, and the basic properties ([ThetaKernelFundamentalProperties.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaKernelFundamentalProperties.lean#L14)) only pass it on to them. The same file gives the basic properties a second name, for fundamental properties of the theta kernel, at line 42. The statement of the basic properties is defined in [CTSmallCone.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CTSmallCone.lean#L138). We have not opened the bound on lattice sums, the common denominator, the archimedean decay, the existence of the admissible form or the rational Darboux lemma.
