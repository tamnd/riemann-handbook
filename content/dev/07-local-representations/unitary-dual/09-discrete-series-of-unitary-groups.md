---
title: Discrete series of unitary groups
decls:
  - PositivityTheory.RgHe.occ
  - PositivityTheory.RgHe3.base
  - PositivityTheory.RgHe3.far_closed
  - PositivityTheory.RgFd.B.formalDegreeCompactDual
  - PositivityTheory.RgFd.B.fdAll
  - PositivityTheory.RgFd.fdAll_of_key
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Discrete series of unitary groups

At the archimedean places, the unitary representations that the global argument needs are the discrete series of the indefinite unitary groups $\mathrm{U}(p, q)$. This section proves two facts about them. The first is a branching statement: under conditions on the Harish-Chandra parameters, a discrete series of $\mathrm{U}(p', q')$ occurs in the restriction of a discrete series of a unitary group of rank one larger. The second is Harish-Chandra's formula for the formal degree: with the Haar measure normalized by the compact dual, the formal degree equals the Weyl dimension of the representation of $\mathrm{U}(n)$ with the same infinitesimal character. The branching statement is the input of [the real input E](/entry/real-input-e-holds/), and the formal degree formula is the input of [the formal degree statement of the literature](/entry/formal-degree-compact-dual-of-literature/). Both enter step [EveryCharacter](/step/every-character/) through the archimedean components.

Background: [representations of real groups](/learn/representations/#representations-of-real-groups), [discrete series](/learn/representations/#discrete-series), [highest weights and branching](/learn/representations/#highest-weights-and-branching).

### Unitary groups and parameters

A *sign vector* is a map $\varepsilon : \{1, \dots, n\} \to \{+, -\}$. Let $J_\varepsilon$ be the diagonal matrix with entries $\pm 1$ given by $\varepsilon$, and let
$$\mathrm{U}_\varepsilon = \{ g \in \mathrm{GL}_n(\mathbb{C}) : g^* J_\varepsilon g = J_\varepsilon \}.$$
If $\varepsilon$ has $p$ plus signs and $q$ minus signs, then $\mathrm{U}_\varepsilon \cong \mathrm{U}(p, q)$. A maximal compact subgroup is $K_\varepsilon \cong \mathrm{U}(p) \times \mathrm{U}(q)$, the stabilizer of the two sign spaces.

A *Harish-Chandra parameter* is a vector $\lambda \in \mathbb{R}^n$ with $\lambda_1 > \lambda_2 > \dots > \lambda_n$ and $\lambda_a - \frac{n-1}{2} \in \mathbb{Z}$ for all $a$. The pair $(\varepsilon, \lambda)$ assigns the entry $\lambda_a$ to the coordinate $a$ of sign $\varepsilon_a$. By Harish-Chandra's theorem, it determines one discrete series of $\mathrm{U}_\varepsilon$: the irreducible unitary representation $\pi_{\varepsilon, \lambda}$ with infinitesimal character $\lambda$ whose matrix coefficients are square-integrable, and whose lowest $K_\varepsilon$-type has highest weight $\lambda + \rho_n - \rho_c$. Here $\rho_c$ and $\rho_n$ are the half sums of the compact and the noncompact positive roots for the chamber of $\lambda$.

### Branching

Let $\varepsilon$ have length $n + 1$ and $\varepsilon'$ length $n$. Embed $\mathrm{U}_{\varepsilon'}$ in $\mathrm{U}_\varepsilon$ as the stabilizer of one coordinate vector of sign $+$, with $\varepsilon'$ the restriction of $\varepsilon$ to the other coordinates. Let $\lambda$ and $\mu$ be Harish-Chandra parameters for $\varepsilon$ and $\varepsilon'$. Merge the $2n + 1$ entries of $\lambda$ and $\mu$ into one list in decreasing order. The pair satisfies *He's condition* if, for any two adjacent entries of the list, the following holds: if both are from $\lambda$ or both from $\mu$, their signs differ; if one is from $\lambda$ and one from $\mu$, their signs agree.

**Theorem 7.9.1 (Branching).** Let $n \ge 2$, and let $\varepsilon$ have $q \ge 1$ minus signs and $p \ge q$ plus signs. Let $\lambda$ and $\mu$ satisfy He's condition, and assume that entries of opposite signs differ by at least $200(n+1)^3$, in $\lambda$ and in $\mu$. Then there is a nonzero bounded map $j : \pi_{\varepsilon', \mu} \to \pi_{\varepsilon, \lambda}$ that intertwines the action of $\mathrm{U}_{\varepsilon'}$.

Lean: `PositivityTheory.RgHe.occ`.

The theorem is a case of the result of H. He on the Gan, Gross and Prasad problem for discrete series of $\mathrm{U}(p, q)$. The proof has three parts.

**Proposition 7.9.2 (Far parameters).** Let $d \in \mathbb{R}^{n+1}$ and $d' \in \mathbb{R}^n$ with $d'_a - d'_b \ge 1$ for $a < b$, and assume that $d'$ is the projection of $d$ under a conjugation by some $g \in \mathrm{U}_\varepsilon$: $\mathrm{tr}(\mathrm{diag}(d)\, g^{-1} Y g) = \mathrm{tr}(\mathrm{diag}(d') Y)$ for all $Y$ in the Lie algebra of $\mathrm{U}_{\varepsilon'}$. Then there are $C$ and $t_0$ with the following property. For $t \ge t_0$, if $\lambda + t d$ is a Harish-Chandra parameter with large gaps, there is a Harish-Chandra parameter $\mu$ with $|\mu_a - t d'_a| \le C \sqrt{t}$ for all $a$, such that every discrete series with parameter $(\varepsilon', \mu)$ maps nontrivially into $\pi_{\varepsilon, \lambda + t d}$.

Lean: `PositivityTheory.RgHe3.far_closed`.

*Proof.* The proof follows Harish-Chandra's method of descent. Restrict $\pi = \pi_{\varepsilon, \lambda + td}$ to $\mathrm{U}_{\varepsilon'}$. The Casimir operators of $\mathrm{U}_\varepsilon$ and of $K_\varepsilon$ act on the smooth vectors, and a square identity relates the Casimir operator of $\mathrm{U}_{\varepsilon'}$ to these operators and to the noncompact root vectors. From this identity one gets bounds on the matrix entries of the root vectors, a bound on the second moment of the moment map $d'$ on a lowest $K_{\varepsilon'}$-type vector, and an approximation of that vector by vectors on which the Casimir operators act by scalars. Markov's inequality then finds a $K_{\varepsilon'}$-finite vector $x \ne 0$ whose quadratic form for $t d'$ is at most $C t \|x\|^2$. Its component in the discrete part of the restriction lies in a discrete series of $\mathrm{U}_{\varepsilon'}$ whose parameter is within $C\sqrt{t}$ of $t d'$. Integrality of the weights and of the half sums of roots makes that parameter a Harish-Chandra parameter. $\square$

**Proposition 7.9.3 (Base case).** Assume, in addition to the hypotheses of the theorem, that every discrete series with parameters $(\varepsilon, \lambda)$ and $(\varepsilon', \mu)$ that occurs in one model occurs in every model, and that the geometric frame below exists. Then there is a map $a$ from the entries of $\lambda$ and $\mu$ to $\mathbb{Z}_{\ge 0}$, increasing with the entry, such that the shifted pair $(\lambda + a, \mu + a)$ has the branching property.

Lean: `PositivityTheory.RgHe3.base`.

The frame hypothesis says: for distinct real vectors $d, d'$ that satisfy He's condition, there is $g \in \mathrm{U}_\varepsilon$ with the projection property of the proposition on far parameters, and a constant $C$ that bounds the size of $h - 1$ for $h \in \mathrm{U}_{\varepsilon'}$ by $C$ times the size of $h$ times the distance from $\mathrm{diag}(d)$ to its conjugate by $g^{-1} h g$.

*Proof.* Twice each entry of $\lambda$ and $\mu$ is an integer. Choose $d$ and $d'$ with the same order and the same signs as $\lambda$ and $\mu$, and take $g$ from the frame. By the proposition on far parameters, for large $t$ the representation $\pi_{\varepsilon, \lambda + td}$ contains a discrete series of $\mathrm{U}_{\varepsilon'}$ with parameter $\mu_t$ close to $t d'$. The frame bound forces $\mu_t$ to keep the interlacing of $t d$ and $t d'$, so $\mu_t - \mu$ is increasing in the entries for $t$ large. Put $a = t d - \lambda$ on the entries of $\lambda$ and $a = \mu_t - \mu$ on those of $\mu$. Since occurrence does not depend on the model, this gives the branching property for the shifted pair. $\square$

*Proof of the theorem.* Decreasing one entry $\lambda_s$ by $1$ keeps the branching property, provided the new pair is again admissible and $\lambda_s - \frac12$ is not an entry of $\mu$: the intertwining map is moved along a decomposition of the tensor product with the standard representation. The same holds for an entry of $\mu$. By the base case, the shifted pair $(\lambda + a, \mu + a)$ has the property. Since $a$ is increasing in the entries, one can walk back from $(\lambda + a, \mu + a)$ to $(\lambda, \mu)$ by steps of $-1$ on single entries that never cross an entry of the other list. Each step keeps the property. $\square$

### Formal degrees

Let $\mu_{\mathrm{cd}}$ be the Haar measure on $\mathrm{U}_\varepsilon$ that is compatible with the Haar measure of total mass $1$ on the compact dual $\mathrm{U}(n)$. A discrete series $\pi$ has *formal degree* $d_\pi > 0$ if
$$\int_{\mathrm{U}_\varepsilon} \langle w, \pi(g) v \rangle\, \overline{\langle w', \pi(g) v' \rangle}\, d\mu_{\mathrm{cd}}(g) = \frac{\langle v', v \rangle \langle w, w' \rangle}{d_\pi}$$
for all vectors $v, w, v', w'$. Let
$$\dim V_\lambda = \prod_{a < b} \frac{\lambda_a - \lambda_b}{b - a},$$
the Weyl dimension of the irreducible representation of $\mathrm{U}(n)$ with infinitesimal character $\lambda$.

**Theorem 7.9.4 (Formal degree).** For every sign vector $\varepsilon$ and Harish-Chandra parameter $\lambda$, the discrete series $\pi_{\varepsilon, \lambda}$ has formal degree $\dim V_\lambda$ for $\mu_{\mathrm{cd}}$. Equivalently, for every unit vector $w$,
$$\int_{\mathrm{U}_\varepsilon} |\langle w, \pi_{\varepsilon, \lambda}(g) w \rangle|^2\, d\mu_{\mathrm{cd}}(g) = \frac{1}{\dim V_\lambda}.$$

Lean: `PositivityTheory.RgFd.B.formalDegreeCompactDual` (also `PositivityTheory.RgFd.B.fdAll`).

The proof builds an explicit model and computes the integral there.

**Proposition 7.9.5 (Formal degree from a model).** Assume two facts on the explicit model below: the subspaces of its lowest $K$-type space are controlled by one equivariant map (the key identity), and the model is a discrete series with parameter $(\varepsilon, \lambda)$ whose $K$-types lie in the cone over the lowest one (the Hilbert space realization). Then the theorem on formal degrees holds.

Lean: `PositivityTheory.RgFd.fdAll_of_key`.

*Proof.* Let $T$ be the lowest $K_\varepsilon$-type, with highest weight $\lambda + \rho_n - \rho_c$. There is an explicit function $\Psi$ on $\mathrm{U}_\varepsilon$ with values in $\mathrm{End}(T)$, built from the polar decomposition $g = k \exp(X)$ and powers of a positive function, that transforms on both sides by $T$. Let $H_\lambda$ be the closed subspace of $L^2(\mathrm{U}_\varepsilon)$ generated by the right translates of the functions $g \mapsto \langle v', \Psi(g) v \rangle$. The first step is the norm identity
$$\int_{\mathrm{U}_\varepsilon} \|\Psi(g)\|_{\mathrm{HS}}^2\, d\mu_{\mathrm{cd}}(g) = \frac{(\dim T)^2}{\dim V_\lambda}.$$
In particular $\Psi$ is square-integrable. By the two assumptions, $H_\lambda$ is stable under right translation and realizes $\pi_{\varepsilon, \lambda}$. A map from $T$ to $H_\lambda$ that is $K$-equivariant and orthogonal to the image of the lowest $K$-type is zero. This gives the matrix coefficient identity: for the unit vector $u_v$ of $H_\lambda$ attached to $v \in T$, $\langle u_{v'}, \pi(g) u_v \rangle$ is a fixed multiple of $\langle v', \Psi(g) v \rangle$. The norm identity then gives the Schur orthogonality relation with constant $\dim V_\lambda$. Two discrete series with the same parameter are isomorphic, so the formal degree is the same for every model. $\square$

The norm identity is proved by induction on $n$. When $q = 0$ the group is compact, and it is Schur orthogonality on $\mathrm{U}(n)$. When $p, q \ge 1$, replace $\lambda$ by $\lambda + t\delta$, with $\delta$ the determinant weight and $t \in \mathbb{Z}_{\ge 0}$. The function $\Psi$ changes by the $t$-th power of a function $U$ with $0 \le U \le 1$. For $t$ large the gaps of $\lambda + t\delta$ are large, and an asymptotic estimate gives the identity, with a right side of the form $c / \prod_i (\alpha_i + t\beta_i)$. A moment lemma then gives the value at $t = 0$: if $\int h U^t\, dP = c / \prod_i (\alpha_i + t \beta_i)$ for all large $t$, then $\int_{U > 0} h\, dP = c / \prod_i \alpha_i$. The set where $U = 0$ is a null set for $\Psi$.

**Remark 7.9.6 (Formalization).** The branching theorem is in [Occ.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/WeightOccurrence/Occ.lean#L10), and the statements of He's condition, the base case and the frame are in [OccSome.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/WeightOccurrence/OccSome.lean#L49). The proposition on far parameters and the base case are in [FarClosed.lean](lean:Development/WeilBound/RepresentationTheoryGL/HolomorphicDiscreteSeries/HarishChandraDescent/FarClosed.lean#L31), with the base case at line 44. The base case takes the independence of the model and the frame as hypotheses; they are supplied only in the final assembly of the theorem. He's condition is defined twice with the same text, in [HeBranching.lean](lean:Development/WeilBound/CoreStatements/BranchingTraces/HeBranching.lean#L28) and in [a second HeBranching.lean](lean:Development/AutomorphicSpectrum/Definitions/MetricPeriods/HeBranching.lean#L31). The theorem covers only parameters with gaps of at least $200(n+1)^3$ and groups with $p \ge q \ge 1$. The formal degree theorem is in [FdTopB.lean](lean:Development/WeilBound/RepresentationTheoryGL/DiscreteSeries/DiscreteSeriesCovers/FdTopB.lean#L9), and the reduction to the model in [ExplicitFunctionSquareIntegrable.lean](lean:Development/WeilBound/RepresentationTheoryGL/FormalDegree/FormalDegreeHilbert/ExplicitFunctionSquareIntegrable.lean#L13), which takes the key identity and the Hilbert space realization as hypotheses. The change from $\mu_{\mathrm{cd}}$ to the measure of the published statement is in [NormIndOfSteps.lean](lean:Development/WeilBound/RepresentationTheoryGL/FormalDegree/FormalDegreeHilbert/NormIndOfSteps.lean#L46), under a name that refers to the metaplectic group, although nothing in it is metaplectic. The norm induction and the moment lemma are stated in [HlamStable.lean](lean:Development/WeilBound/RepresentationTheoryGL/FormalDegree/FormalDegreeHilbert/HlamStable.lean#L76) and [MomB.lean](lean:Development/WeilBound/RepresentationTheoryGL/FormalDegree/FormalDegreeHilbert/MomB.lean#L19).
