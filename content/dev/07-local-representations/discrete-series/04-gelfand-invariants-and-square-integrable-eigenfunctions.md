---
title: Gelfand invariants and square integrable eigenfunctions
decls:
  - ReciprocityTheory.ChartRestriction.DS.r0bG
  - ReciprocityTheory.ChartRestriction.DS.S7.psiM_local
  - ReciprocityTheory.ChartRestriction.DS.S7.gelfand_psM
  - ReciprocityTheory.ChartRestriction.DS.S7.psiM_gelfand
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gelfand invariants and square integrable eigenfunctions

A discrete series of $U(p,q)$ is detected by its matrix coefficients: they are square integrable eigenfunctions of the center of the enveloping algebra. This section proves two facts about such functions. The first is a regularity statement: if a finite-dimensional space of weighted square integrable functions is stable under $\mathfrak{k}$ and the Casimir operator acts on it by a scalar, then all its derivatives stay weighted square integrable, and the Lie algebra acts by skew-adjoint operators. The second is the construction of an explicit operator-valued function $\Psi$ on $U(p,q)$, built from a $K$-type and from powers of leading principal minors, together with the eigenvalues of all Gelfand invariants on $\Psi$. Both are used in the step [EveryCharacter from the literature](/step/every-character-of-literature/), where the infinitesimal character of a discrete series is read off.

Background: [the center of $U(\mathfrak{g})$ and the Casimir operator](/learn/real-groups/#the-center-of-umathfrakg-and-the-casimir-operator), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [highest weights and branching](/learn/representations/#highest-weights-and-branching), [[Harish-Chandra module|2MKHH636C3]].

### The operators $E_{ab}$

We keep $G_\varepsilon \cong U(p,q)$, $K_\varepsilon \cong U(p) \times U(q)$ and $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$ from [the section on polar coordinates](/entry/mu-polar-is-haar/). Let $dg$ be a Haar measure on $G_\varepsilon$.

**Definition 3.4.1 (Right derivatives).** For a function $f$ on $G_\varepsilon$ and $X \in \mathfrak{g}$, let $R_X f(g) = \frac{d}{dt} f(g \exp(tX))\big|_{t=0}$. For $Z \in M_n(\mathbb{C}) = \mathfrak{g} \oplus i\mathfrak{g}$, write $Z = X + iY$ with $X, Y \in \mathfrak{g}$ and put $R_Z = R_X + i R_Y$. Let $E_{ab} = R_{e_{ab}}$, where $e_{ab}$ is the matrix unit. For a word $w = (a_1 b_1, \dots, a_m b_m)$ let $E_w = E_{a_1 b_1} \cdots E_{a_m b_m}$. The *Casimir operator* is $\Omega = \sum_{a,b} E_{ab} E_{ba}$.

Put $s(a,b) = 1$ if $\varepsilon_a = \varepsilon_b$ and $s(a,b) = -1$ otherwise. On a unitary representation of $G_\varepsilon$ the derived action satisfies $\langle E_{ab} x, y \rangle = s(a,b) \langle x, E_{ba} y\rangle$, since $e_{ab}^* = e_{ba}$ and $i\mathfrak{p}$ is Hermitian while $\mathfrak{k}$ is skew-Hermitian. The pairs $(a,b)$ with $\varepsilon_a = \varepsilon_b$ span $\mathfrak{k}_{\mathbb{C}}$.

Let $\|g\|^2 = \sum_{a,b} |g_{ab}|^2$ be the squared Hilbert-Schmidt norm. It is at least $n$ on $G_\varepsilon$ and grows exponentially along $\exp(t X)$ for $X \in \mathfrak{p}$, so the weight $\|g\|^{4a}$ measures decay of a function.

**Theorem 3.4.2 (Weighted square integrability of derivatives).** Let $W$ be a finite-dimensional space of smooth functions on $G_\varepsilon$. Let $c \in \mathbb{C}$ and $a \geq 0$. Assume:

1. for every $w \in W$ and every $(i,j)$ with $\varepsilon_i = \varepsilon_j$, the function $E_{ij} w$ lies in $W$;
2. $\Omega w = c\, w$ for every $w \in W$;
3. $\int_{G_\varepsilon} \|g\|^{4a} |w(g)|^2\, dg < \infty$ for every $w \in W$.

Then for all words $w_1, w_2$ and all $f, f' \in W$: the function $E_{w_1} f$ is smooth, $\int \|g\|^{4a} |E_{w_1} f(g)|^2\, dg < \infty$, and for all $i, j$,
$$\int_{G_\varepsilon} E_{ij} E_{w_1} f \cdot \overline{E_{w_2} f'}\; dg = s(i,j) \int_{G_\varepsilon} E_{w_1} f \cdot \overline{E_{ji} E_{w_2} f'}\; dg.$$

Lean: `ReciprocityTheory.ChartRestriction.DS.r0bG`.

*Proof.* The proof uses two analytic facts. First, $h(g) = \log \|g\|^2$ is smooth on $G_\varepsilon$ and Lipschitz: $|R_X h(g)| \leq 2 \|X\|$ for $X \in \mathfrak{g}$. Second, for a smooth function $\varphi$ that vanishes where $\|g\|^2$ is large, $\int R_X \varphi\, dg = 0$, by invariance of $dg$ under right translation by $\exp(tX)$. With these, one works on the filtration of $U(\mathfrak{g}_{\mathbb{C}}) W$ by the length of words. Since $\Omega$ acts by $c$ and $W$ is stable under $\mathfrak{k}_{\mathbb{C}}$, the operator $\sum_{a,b} s(a,b) E_{ab} E_{ba}$, which differs from $\Omega$ by twice the $\mathfrak{p}$ part, keeps each step of the filtration modulo the previous one. Multiply by a cutoff function of $h$ and integrate by parts with the second fact. The Lipschitz bound controls the derivative of the cutoff and of the weight $e^{2a h} = \|g\|^{4a}$. This shows by induction on the length that $\|g\|^{4a} |E_w f|^2$ is integrable for every word $w$. The pairing identity then follows from the second fact applied to $E_{w_1} f \cdot \overline{E_{w_2} f'}$ times a cutoff, and a limit, since the boundary terms are integrable. $\square$

### The function $\Psi$

Let $\lambda \in \mathbb{R}^n$. Let $\rho_a = (n-1)/2 - a$ for $a = 0, \dots, n-1$. Let $\rho_{\mathfrak{k}}$ and $\rho_{\mathfrak{n}}$ be the half sums for the compact and the noncompact pairs:
$$\rho_{\mathfrak{k},a} = \tfrac12\bigl(\#\{b > a : \varepsilon_b = \varepsilon_a\} - \#\{b < a : \varepsilon_b = \varepsilon_a\}\bigr),$$
and $\rho_{\mathfrak{n},a}$ the same with $\varepsilon_b \neq \varepsilon_a$. Let $\Lambda_K(\lambda) = \lambda + \rho_{\mathfrak{n}} - \rho_{\mathfrak{k}}$. When $\lambda$ is the Harish-Chandra parameter of a discrete series, $\Lambda_K(\lambda)$ is the Blattner parameter, the highest weight of its lowest $K$-type (Hecht-Schmid; see the Notes at the end of the chapter).

**Definition 3.4.3 ($K$-type).** A *$K$-type of highest weight $\Lambda$* is a finite-dimensional irreducible continuous unitary representation $(\tau, V)$ of $K_\varepsilon$, with derived action $d\tau$, and a unit vector $w \in V$ with $d\tau(e_{aa}) w = \Lambda_a w$ for all $a$ and $d\tau(e_{ab}) w = 0$ for $a < b$ with $\varepsilon_a = \varepsilon_b$.

**Definition 3.4.4 (The function $\Psi$).** Let $\mu \in \mathbb{Z}^n$ with $\mu_a = \lambda_a + \rho_a$ for all $a$, and put $\mu_n = 0$. For $z \in M_n(\mathbb{C})$ let $\Delta_i(z)$ be the leading principal $i \times i$ minor, and
$$\Phi_\mu(z) = \prod_{i=1}^{n} \Delta_i(z)^{-(\mu_{i-1} - \mu_i)}.$$
Let $P_w$ be the orthogonal projection on $\mathbb{C} w$, and $dk$ the Haar probability measure on $K_\varepsilon$. Put
$$\psi(z) = \dim V \int_{K_\varepsilon} \Phi_\mu(k^{-1} z k)\; \tau(k) P_w \tau(k)^{-1}\, dk \in \operatorname{End}(V).$$
For $g = k \exp(X) \in G_\varepsilon$ with $k \in K_\varepsilon$ and $X \in \mathfrak{p}$, put $\Psi(g) = \tau(k)\, \psi(\exp X)$.

The function $\Phi_\mu$ is holomorphic where the minors do not vanish, in particular near the positive definite matrices. The average over $K_\varepsilon$ makes $\psi$ equivariant: $\psi(k z k^{-1}) = \tau(k)\psi(z)\tau(k)^{-1}$.

**Lemma 3.4.5 (Local holomorphic formula for $\Psi$).** Let $T = (\tau, V, w)$ be a $K$-type of highest weight $\Lambda_K(\lambda)$, and let $\mu$ be as above. Let $U$ be an open set of matrices that contains all positive definite matrices, and let $g_0 \in G_\varepsilon$. There are an open set $W \ni g_0$ and $k_0 \in K_\varepsilon$ such that every $g \in W$ is invertible with $g^{-1} k_0 \in U$, and
$$\Psi(g) = \tau(k_0)\, \psi(g^{-1} k_0) \quad\text{for all } g \in W \cap G_\varepsilon.$$

Lean: `ReciprocityTheory.ChartRestriction.DS.S7.psiM_local`.

*Proof.* Let $g = k(g)\exp(L(g))$ be the polar decomposition, so $k(g) = g \exp(-L(g))$ depends continuously on $g \in G_\varepsilon$. Take $k_0 = k(g_0)$. For $g$ near $g_0$, $k(g)^{-1} k_0$ is near $1$ and equals $\exp(Y)$ for a small $Y \in \mathfrak{k}$. Then $g^{-1} k_0 = \exp(-L(g))\exp(Y)$, and the path $t \mapsto \exp(-L(g))\exp(tY)$, $t \in [0,1]$, stays in $U$ by compactness of $[0,1]$, since at $g = g_0$ it is the positive definite matrix $\exp(-L(g_0))$. The formula follows from the equivariance of $\psi$ under $K_\varepsilon$ and from the definition of $\Psi$, using that $\psi$ is holomorphic on a neighborhood of the positive definite matrices on which this identity holds. $\square$

### Gelfand invariants

**Definition 3.4.6 (Gelfand operators).** Let $A = (A_{ab})_{a,b \leq n}$ be a matrix of linear operators on a vector space. Define $(A^0)_{ab} = \delta_{ab}$ and $(A^{k+1})_{ab} = \sum_c A_{ac} (A^k)_{cb}$. The *$k$-th Gelfand operator* is $\Gamma_k(A) = \sum_a (A^k)_{aa}$.

For $A = (E_{ab})$ the operators $\Gamma_k(E)$ are the Gelfand invariants. They are central in $U(\mathfrak{gl}_n)$, so they act by scalars on functions that generate an irreducible representation. The scalars are given by a generating series.

**Definition 3.4.7 (Gelfand values).** For $l \in \mathbb{C}^n$ and $k \geq 0$ let $\gamma_k(l)$ be the coefficient of $X^{k+1}$ in the power series
$$1 - \prod_{r=1}^{n} \Bigl(1 - \frac{X}{1 - l_r X}\Bigr).$$
For $\lambda \in \mathbb{R}^n$ let $\ell(\lambda)_r = \lambda_r + (n-1)/2$.

For example, $\gamma_0(l) = n$ and $\gamma_1(l) = \sum_r l_r - \binom{n}{2}$.

We need two holomorphic versions of $E_{ab}$. For a holomorphic function $F$ near $z$, let $L_X F(z) = dF_z(Xz)$, the derivative along left multiplication.

**Proposition 3.4.8 (Gelfand eigenvalues of $\psi$).** Let $T$ be a $K$-type of any highest weight, $\lambda \in \mathbb{R}^n$ and $\mu \in \mathbb{Z}^n$ with $\mu_a = \lambda_a + \rho_a$. There is an open set $U$ containing all positive definite matrices on which $\psi$ is holomorphic, and for all $z \in U$ and $k \geq 0$,
$$\begin{aligned}
\Gamma_k\bigl(L_{e_{ab}}\bigr)\psi(z) &= (-1)^k \gamma_k\bigl(\ell(\lambda)\bigr)\, \psi(z), \\
\Gamma_k\bigl(L_{e_{\bar b \bar a}}\bigr)\psi(z) &= \gamma_k\bigl(\ell(-\lambda)\bigr)\, \psi(z),
\end{aligned}$$
where $\bar a = n - 1 - a$ is the reversed index.

Lean: `ReciprocityTheory.ChartRestriction.DS.S7.gelfand_psM`.

*Proof.* The Gelfand operators commute with conjugation $z \mapsto k^{-1} z k$: conjugating the matrix $(L_{e_{ab}})$ by $k$ changes it to $(\sum k_{ac} L_{e_{cd}} (k^{-1})_{db})$, and the trace of the $k$-th power is invariant. So it suffices to prove the two identities for $\Phi_\mu$ in place of $\psi$, on the open set where all leading minors are nonzero. There they hold with the same scalars: $\Gamma_k(L_{e_{ab}})\Phi_\mu = (-1)^k \gamma_k(\ell(\lambda))\Phi_\mu$ and $\Gamma_k(L_{e_{\bar b \bar a}})\Phi_\mu = \gamma_k(\ell(-\lambda))\Phi_\mu$. This is a computation with the leading minors: $L_{e_{ab}}$ with $a > b$ kills each $\Delta_i$ (adding a multiple of an earlier row to a later row), and $L_{e_{aa}}$ multiplies $\Delta_i$ by $1$ or $0$, so $\Phi_\mu$ is a weight vector annihilated by one triangular half, and the Gelfand invariants act on it by their values at the weight, shifted by $\rho$. The second identity follows from the first after reversing the order of the indices. Then integrate over $K_\varepsilon$; the open set $U$ can be chosen so that $k^{-1}zk$ lies in the domain of $\Phi_\mu$ for all $k$. $\square$

**Theorem 3.4.9 (Gelfand eigenvalues of $\Psi$).** Let $T$ be a $K$-type of highest weight $\Lambda_K(\lambda)$, and let $\mu \in \mathbb{Z}^n$ with $\mu_a = \lambda_a + \rho_a$. For every $g \in G_\varepsilon$ and $k \geq 0$,
$$\Gamma_k(E)\Psi(g) = \gamma_k\bigl(\ell(\lambda)\bigr)\Psi(g), \qquad \Gamma_k(E^{\mathrm{rev}})\Psi(g) = \gamma_k\bigl(\ell(-\lambda)\bigr)\Psi(g),$$
where $E^{\mathrm{rev}}_{ab} = -E_{\bar b \bar a}$.

Lean: `ReciprocityTheory.ChartRestriction.DS.S7.psiM_gelfand`.

*Proof.* Fix $g$. By [Lemma 3.4.5](/entry/psi-m-local/), on a neighborhood of $g$ in $G_\varepsilon$ we have $\Psi(g') = \tau(k_0)\psi(g'^{-1} k_0)$, with $g'^{-1} k_0$ in the open set of [Proposition 3.4.8](/entry/gelfand-ps-m/). The right derivative $E_{ab}$ of $g' \mapsto \psi(g'^{-1}k_0)$ is $-L_{e_{ab}}\psi$ evaluated at $g'^{-1}k_0$, because $(g' e^{tX})^{-1} = e^{-tX} g'^{-1}$. So $\Gamma_k(E)\Psi(g) = (-1)^k \tau(k_0)\,\Gamma_k(L_{e_{ab}})\psi(g^{-1}k_0)$, and the Proposition gives $(-1)^k (-1)^k \gamma_k(\ell(\lambda)) = \gamma_k(\ell(\lambda))$. For $E^{\mathrm{rev}}$ the two signs give $(-(-1))^k = 1$, and the second identity of the Proposition applies. $\square$

**Remark 3.4.10 (Formalization).** The weighted square integrability theorem assumes that $W$ is finite-dimensional, but the proof discards this hypothesis ([IntegrableComplexContinuousBoundedSupport.lean](lean:Formalism/RealPlaceAnalysis/RealPlaceTaylor/IntegrableComplexContinuousBoundedSupport.lean#L1498)). Its two analytic inputs (the Lipschitz bound and the vanishing of integrals of derivatives) are separate theorems passed as arguments; the proof sketch above is the order of the formal proof, but we have not opened every lemma of the induction. The function $\Psi$ is defined by a choice of polar decomposition, and is set to $0$ off $G_\varepsilon$. The proposition on $\psi$ allows any highest weight; only the theorem on $\Psi$ needs $\Lambda_K(\lambda)$. Two proofs in this group try several instance choices in turn with `first` ([PsiMLocal.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/CasimirCoefficients/PsiMLocal.lean#L30), [GelfandPs.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/CasimirCoefficients/GelfandPs.lean#L54)). The identities for $\Phi_\mu$ are a separate lemma ([GelfandPhi.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/CasimirCoefficients/GelfandPhi.lean#L133)); we read its statement, not its proof, so the explanation of the scalars is the classical one.
