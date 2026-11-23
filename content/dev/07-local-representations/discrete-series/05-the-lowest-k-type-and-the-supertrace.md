---
title: The lowest K-type and the supertrace
decls:
  - ReciprocityTheory.ChartRestriction.DS.Lap.LemK.lowestKType_casimir_cone
  - ReciprocityTheory.ChartRestriction.DS.TRGap.ker_D_eq_kLowSpan
  - ReciprocityTheory.ChartRestriction.DS.TRGap.supTrace
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The lowest K-type and the supertrace

A discrete series representation $\sigma$ of $U(p,q)$ is not finite-dimensional, but some of its averages over the maximal compact subgroup $K$ have finite rank. This section proves a trace formula for such averages. If $B = \int_K P(k) \det(1 - \operatorname{Ad}(k)|_{\mathfrak{p}^+})\, \sigma(k)\, dk$ for a polynomial $P$ in the matrix entries, then $B$ has finite rank, and its trace is $\pm$ the integral of $P$ against the character of one explicit $K$-type. The proof goes through a Dirac type operator on $\sigma \otimes \bigwedge \mathfrak{p}^+$, whose kernel is computed with the lowest $K$-type of $\sigma$. The result is used in [Theorem 2.1.4 of Volume 8](/entry/exists-type/) of the chapter on the unitary trace formula.

Background: [the Casimir operator](/learn/real-groups/#the-center-of-umathfrakg-and-the-casimir-operator), [discrete series and formal degrees](/learn/real-groups/#discrete-series-and-formal-degrees), [admissible representations and $(\mathfrak{g},K)$-modules](/learn/real-groups/#admissible-representations-and-mathfrakg-k-modules), [highest weights](/learn/representations/#highest-weights-and-branching), [[Harish-Chandra module|2MKHH636C3]], [[unitary representation|74BPYJNZTM]].

### Notation

We keep the notation of the previous section: $\varepsilon \in \{+,-\}^n$ has $p$ plus signs and $q$ minus signs, $J_\varepsilon = \operatorname{diag}(\varepsilon_1, \dots, \varepsilon_n)$, $G_\varepsilon = \{ g : g^* J_\varepsilon g = J_\varepsilon \} \cong U(p,q)$, and $K_\varepsilon$ is the group of unitary matrices that commute with $J_\varepsilon$, so $K_\varepsilon \cong U(p) \times U(q)$. A pair $(a,b)$ is *compact* if $\varepsilon_a = \varepsilon_b$ and *noncompact* if not. We index $\{1, \dots, n\}$ from $0$ where a formula needs it, and put $q_0 = \min(p,q)$.

Weights are vectors in $\mathbb{R}^n$, and $e_a$ is the $a$-th unit vector. Put $\rho(a) = (n-1)/2 - a$,
$$\rho_k(a) = \tfrac12\bigl(\#\{b > a : \varepsilon_b = \varepsilon_a\} - \#\{b < a : \varepsilon_b = \varepsilon_a\}\bigr),$$
and $\rho_n$ by the same formula with $\varepsilon_b \neq \varepsilon_a$. Put $\rho_h(a) = q/2$ if $\varepsilon_a = +$ and $\rho_h(a) = -p/2$ if $\varepsilon_a = -$. For $\lambda \in \mathbb{R}^n$ put
$$\Lambda_K(\lambda) = \lambda + \rho_n - \rho_k, \qquad \gamma(\lambda) = \lambda - \rho_k + \rho_h, \qquad c(\lambda) = |\lambda|^2 - |\rho|^2.$$
A weight $\beta$ is in the *root cone* if $\beta = \sum_{a<b} m_{ab}(e_a - e_b)$ with all $m_{ab} \in \mathbb{N}$.

**Definition 3.5.1 (Gap and threshold).** Let $h \in \mathbb{R}$. The weight $\lambda$ has *gap at least $h$* if $h \leq |\lambda_a - \lambda_b|$ for every noncompact pair $(a,b)$. The *threshold* is
$$\theta_\varepsilon = \max\bigl(npq + 1,\ 16\, n\, q_0 + 8\sqrt{2 q_0}\bigr).$$

**Definition 3.5.2 (Derived action).** Let $\sigma$ be a map from $M_n(\mathbb{C})$ to bounded operators on a Hilbert space $H$ whose restriction to $G_\varepsilon$ is a strongly continuous unitary representation. Let $D \subseteq H$ be a subspace and let $E_{ab}$, $1 \leq a,b \leq n$, be linear operators on $D$. We say that $E$ is a *derived action of $\sigma$ on $D$* if:

1. $E_{ab}E_{cd} - E_{cd}E_{ab} = \delta_{bc}E_{ad} - \delta_{da}E_{cb}$ for all $a,b,c,d$;
2. $\sigma(k)D \subseteq D$ for every $k \in K_\varepsilon$;
3. for every $X$ in the Lie algebra of $G_\varepsilon$ and every $v \in D$, the map $t \mapsto \sigma(\exp tX)v$ has derivative $\sum_{a,b} X_{ab}E_{ab}v$ at $t = 0$.

The *Casimir operator* is $\Omega = \sum_{a,b} E_{ab}E_{ba}$. For a subspace $V \subseteq D$, the *generated subspace* $U(\mathfrak{g})V$ is the smallest subspace that contains $V$ and is stable under every $E_{ab}$.

**Definition 3.5.3 ($K$-types of highest weight).** Let $A_{ab}$ be operators on a vector space $M$. A vector $v$ is a *$K$-highest weight vector of weight $\mu$* if $A_{aa}v = \mu_a v$ for every $a$ and $A_{ab}v = 0$ for every compact pair with $a < b$. A subspace $S$ is *$K$-stable* if $A_{ab}S \subseteq S$ for every compact pair. It is *$K$-irreducible of highest weight $\Lambda$* if it is finite-dimensional and $K$-stable, if its only $K$-stable subspaces are $0$ and $S$, and if it contains a nonzero $K$-highest weight vector of weight $\Lambda$.

### The Fock space and the operator $\mathcal{D}$

Let $\mathcal{F} = \bigwedge(\mathbb{C}^{n \times n})$, with basis vectors $f_{ia}$ of $\mathbb{C}^{n \times n}$. Let $c^+_{ia}$ be left multiplication by $f_{ia}$, and let $c^-_{ia}$ be the contraction with the dual vector of $f_{ia}$. On $D \otimes \mathcal{F}$ we use $E_{ab}$ for $E_{ab} \otimes 1$ and $c^\pm_{ia}$ for $1 \otimes c^\pm_{ia}$. Put:

- the *diagonal action* $\widetilde{E}_{ab} = E_{ab} + s_{ab}$, where $s_{ab} = \sum_{\varepsilon_x = -} c^+_{ax}c^-_{bx}$ if $\varepsilon_a = \varepsilon_b = +$, $s_{ab} = -\sum_{\varepsilon_i = +} c^+_{ib}c^-_{ia}$ if $\varepsilon_a = \varepsilon_b = -$, and $s_{ab} = 0$ otherwise;
- the operator $\mathcal{D} = \sum_{\varepsilon_i = +,\ \varepsilon_a = -} \bigl(E_{ai}c^+_{ia} - E_{ia}c^-_{ia}\bigr)$;
- the *physical subspace* $\Phi$, the set of vectors killed by $c^-_{ia}$ for every pair $(i,a)$ that does not satisfy $\varepsilon_i = +$ and $\varepsilon_a = -$;
- the number $s_\varepsilon = \#\{(a,b) : \varepsilon_a = +,\ \varepsilon_b = -,\ b < a\}$;
- for $z \in D \otimes \mathcal{F}$, the *lowering span* $L(z)$: the span of all vectors $\widetilde{E}_{a_1b_1} \cdots \widetilde{E}_{a_rb_r} z$ with $r \geq 0$ and each $(a_j,b_j)$ a compact pair with $b_j < a_j$.

The physical subspace is $D \otimes \bigwedge \mathfrak{p}^+$, where $\mathfrak{p}^+$ is spanned by the $f_{ia}$ with $\varepsilon_i = +$ and $\varepsilon_a = -$.

### The lowest $K$-type generates a cone

The common hypotheses of this section are the following, and we call them *the lowest $K$-type data*. The Hilbert space $H$ is complete; $\sigma$ and $E$ are as in the definition of a derived action on $D$; $V \subseteq D$ is $K$-irreducible of highest weight $\Lambda_K(\lambda)$ for $E$; $\Omega v = c(\lambda)v$ for $v \in V$; $\sigma(k)V \subseteq V$ for $k \in K_\varepsilon$; $\lambda_a - (n-1)/2 \in \mathbb{Z}$ for every $a$; $\lambda$ is strictly decreasing; $\lambda$ has gap at least $h$; $\theta_\varepsilon < h$; and $p, q \geq 1$.

**Theorem 3.5.4 (The lowest $K$-type cone).** Assume the lowest $K$-type data. Let $\mu \in \mathbb{R}^n$ and let $w \in U(\mathfrak{g})V$ be a nonzero $K$-highest weight vector of weight $\mu$ for $E$. Then $\mu - \Lambda_K(\lambda)$ is in the root cone.

Lean: `ReciprocityTheory.ChartRestriction.DS.Lap.LemK.lowestKType_casimir_cone`.

*Proof.* The bound $\theta_\varepsilon < h$ gives $8 n q_0 < h$, and the gap condition then gives the large gap that the auxiliary results need. Fix a $K$-type $T$ of highest weight $\Lambda_K(\lambda)$, a $K$-isomorphism from $T$ to $V$, and a weight $\mu_0$ that is attached to $\lambda$. Pairing with the image $v_0 \in V$ of the highest weight vector of $T$ gives a linear functional on $V$ on which $E_{aa}$ acts through the eigenvalue $\Lambda_K(\lambda)_a$. Lift $w$ to a vector $u$ in a tensor space built on $V$, and apply words in the compact lowering operators to $u$. If every such word were killed by the functional built from $v_0$, then a $K$-stable space in the kernel would exist, and an integral formula over the lowest $K$-type would give $w = 0$. So some word $x$ gives a nonzero value. That value lies in a module generated by one vector of weight $\lambda + \rho$, and it has weight $\nu' - \Lambda_K(\lambda) + \lambda + \rho$, where $\nu'$ is the weight of $x$. Every weight of such a module is the generating weight minus an element of the root cone. The weight $\nu'$ differs from $\mu$ by a sum of compact negative roots. Together these give that $\mu - \Lambda_K(\lambda)$ is in the root cone. $\square$

### The kernel of $\mathcal{D}$

**Theorem 3.5.5 (Kernel of the Dirac operator).** Assume the lowest $K$-type data. There is $z \in D \otimes \mathcal{F}$ with the following properties:

1. $z \neq 0$, and $z \in V \otimes \bigwedge^{s_\varepsilon}(\mathbb{C}^{n \times n})$;
2. $z$ is a $K$-highest weight vector of weight $\gamma(\lambda)$ for the diagonal action $\widetilde{E}$;
3. $\ker \mathcal{D} \cap \bigl(U(\mathfrak{g})V \otimes \mathcal{F}\bigr) \cap \Phi = L(z)$;
4. $L(z)$ is $K$-irreducible of highest weight $\gamma(\lambda)$ for $\widetilde{E}$.

Lean: `ReciprocityTheory.ChartRestriction.DS.TRGap.ker_D_eq_kLowSpan`.

*Proof.* Write $\mathcal{K}$ for the left side of item 3. Since $\sigma$ is unitary, the adjoint of $E_{ab}$ on $D$ is $\pm E_{ba}$, with a sign that depends only on the pair $(a,b)$. By the previous theorem, every $K$-highest weight in $U(\mathfrak{g})V$ is $\Lambda_K(\lambda)$ plus an element of the root cone. The Casimir operator commutes with every $E_{ab}$, so it acts by $c(\lambda)$ on all of $U(\mathfrak{g})V$. A $K$-highest weight vector of weight $\Lambda_K(\lambda)$ in $U(\mathfrak{g})V$ lies in $V$. Next, there is a nonzero $z$ in $V \otimes \bigwedge^{s_\varepsilon}$, in $\Phi$ and in $\ker \mathcal{D}$, of weight $\gamma(\lambda)$ for $\widetilde{E}$. This gives items 1 and 2.

The operators $\widetilde{E}_{ab}$ for compact pairs satisfy the relations of $\mathfrak{gl}$, and they commute with $\mathcal{D}$. So $\mathcal{K}$ is $K$-stable, and $L(z) \subseteq \mathcal{K}$. Every $K$-highest weight vector $y \in \mathcal{K}$ is a multiple of $z$: this is the uniqueness statement, and it uses the cone, the Casimir value and the fact that $\Lambda_K(\lambda)$ occurs only in $V$. Also $L(z) \subseteq V \otimes \mathcal{F}$, so $L(z)$ is finite-dimensional.

For the reverse inclusion, let $Y \subseteq \mathcal{K}$ be finite-dimensional and $K$-stable with $L(z) \subseteq Y$. Let $Y'$ be the orthogonal complement of $L(z)$ in $Y$ for the natural Hermitian form on $D \otimes \mathcal{F}$. Since the adjoint of $\widetilde{E}_{ab}$ for this form is $\pm\widetilde{E}_{ba}$ for compact pairs, and $L(z)$ is $K$-stable, $Y'$ is $K$-stable. If $Y' \neq 0$, it contains a $K$-highest weight vector, which is then $cz$ with $c \neq 0$. But $cz \in L(z)$ is orthogonal to itself, and the form is positive definite, a contradiction. So $Y' = 0$, the pairing of $Y$ with $L(z)$ is injective on $Y$, and $\dim Y \leq \dim L(z)$. Hence $Y = L(z)$. The space $U(\mathfrak{g})V$ is the union of the finite-dimensional $K$-stable spaces $L_j$ defined below, so every vector of $\mathcal{K}$ lies in such a $Y$, and $\mathcal{K} = L(z)$. The same uniqueness of the highest weight vector gives that $L(z)$ is $K$-irreducible. $\square$

### The supertrace formula

For $k \in K_\varepsilon$ let
$$\Delta(k) = \det_{x,y}\bigl(\delta_{xy} - k_{x_1y_1}\,\overline{k_{x_2y_2}}\bigr),$$
where $x = (x_1,x_2)$ and $y = (y_1,y_2)$ run over the pairs with $\varepsilon_{x_1} = +$ and $\varepsilon_{x_2} = -$. The matrix $(k_{x_1y_1}\overline{k_{x_2y_2}})$ is the matrix of $X \mapsto kXk^{-1}$ on $\mathfrak{p}^+$, so $\Delta(k) = \det(1 - \operatorname{Ad}(k)|_{\mathfrak{p}^+})$. A *polynomial in the entries* is a polynomial $P$ in the $2n^2$ variables $k_{ab}$ and $\overline{k_{ab}}$, and $P(k)$ is its value. Let $dk$ be the fixed Haar measure on $K_\varepsilon$.

We say that $\sigma$ is a *discrete series of parameter $\lambda$* if $H$ is complete and nonzero, $\sigma$ is a strongly continuous irreducible unitary representation of $G_\varepsilon$ with square integrable matrix coefficients, and $\sigma$ contains a $K$-type of highest weight $\Lambda_K(\lambda)$ that minimizes $|\mu + 2\rho_k|^2$ among the highest weights $\mu$ of $K$-types of $\sigma$. The weight $\lambda$ is a *Harish-Chandra parameter* if it is strictly decreasing and $\lambda_a - (n-1)/2 \in \mathbb{Z}$ for all $a$.

**Theorem 3.5.6 (Supertrace formula).** Let $\sigma$ be a discrete series of parameter $\lambda$ on $H$, where $\lambda$ is a Harish-Chandra parameter with gap at least $h$ and $\theta_\varepsilon < h$, and let $p, q \geq 1$. There are a nonzero finite-dimensional Hilbert space $W$ and a strongly continuous unitary representation $T$ of $K_\varepsilon$ on $W$ such that $W$ is a $K$-type of highest weight $\gamma(\lambda)$, with the following property. Let $P$ be a polynomial in the entries and let $B$ be a bounded operator on $H$ with
$$B w = \int_{K_\varepsilon} P(k)\, \Delta(k)\, \sigma(k) w \, dk \qquad (w \in H).$$
Then the range of $B$ is finite-dimensional, and the trace of $B$ on its range is
$$\operatorname{tr} B = (-1)^{s_\varepsilon} \int_{K_\varepsilon} P(k) \operatorname{tr} T(k)\, dk.$$

Lean: `ReciprocityTheory.ChartRestriction.DS.TRGap.supTrace`.

*Proof.* From the discrete series hypothesis we get a subspace $D$ of smooth vectors with a derived action $E$, a $K$-irreducible $V \subseteq D$ of highest weight $\Lambda_K(\lambda)$ on which $\Omega$ acts by $c(\lambda)$, and the density of the closure of $U(\mathfrak{g})V$ in $H$. Put $L_0 = V$ and $L_{j+1} = L_j + \sum_{(a,b) \text{ noncompact}} E_{ab}L_j$. Each $L_j$ is finite-dimensional and $K$-stable. The representation $T$ is the $K$-type of the previous theorem: its trace at $k$ is the trace of $k$ on $\mathcal{K} = L(z)$.

The function $\Delta$ is itself a polynomial in the entries, because $\det(1 - A) = \sum_S (-1)^{|S|}\det A_{SS}$ over the principal minors. For every polynomial $R$ in the entries there is $j$ such that $\int R(k)\sigma(k)u\,dk \in L_j$ for all $u \in H$. Take $J$ large enough for $R = P\Delta$ and for the finitely many polynomials that come from the minors. Then the range of $B$ lies in $L_J$, so it is finite-dimensional, and
$$\operatorname{tr} B = \int_{K_\varepsilon} P(k)\,\Delta(k)\, \operatorname{tr}\bigl(\sigma(k)|_{L_J}\bigr)\, dk.$$

Let $\tau$ be the parity operator on $\mathcal{F}$, equal to $(-1)^j$ on $\bigwedge^j$, and let $Y_0 = (L_J \otimes \mathcal{F}) \cap \Phi$. Since $\sum_j (-1)^j \operatorname{tr} \bigwedge^j A = \det(1 - A)$, for each $k$
$$\Delta(k) \operatorname{tr}\bigl(\sigma(k)|_{L_J}\bigr) = \operatorname{tr}\bigl(\tau\, k|_{Y_0}\bigr).$$
Let $Y = Y_0 + \mathcal{D}Y_0$. The integral of $P(k)\operatorname{tr}(\tau k|_Y)$ equals the integral of $P(k)\operatorname{tr}(\tau k|_{Y_0})$, because the averaged operators map $Y$ into $Y_0$. On $Y$, the operator $\mathcal{D}$ commutes with $K$ and exchanges the parities. So the supertrace of $k$ on $Y$ is the supertrace on $\mathcal{K}$, which lies in $Y_0$. By the previous theorem, $\mathcal{K} = L(z)$ with $z$ of degree $s_\varepsilon$, so $\tau = (-1)^{s_\varepsilon}$ on $\mathcal{K}$. Hence $\operatorname{tr}(\tau k|_Y) = (-1)^{s_\varepsilon}\operatorname{tr} T(k)$. Integrate against $P$. $\square$

The operator $\mathcal{D}$ is the algebraic form of the Dirac type operator in the realization of the discrete series by Schmid and by Atiyah and Schmid, and the lowest $K$-type $\Lambda_K(\lambda) = \lambda + \rho_n - \rho_k$ is the one given by the Blattner formula of Hecht and Schmid (see the notes at the end of the chapter).

**Remark 3.5.7 (Formalization).** The threshold is written in two forms: the cone theorem has $\max(npq+1, 16 n \min(p,q) + 8\sqrt{2\min(p,q)})$ written out, and the other two theorems use the named threshold; the kernel theorem converts between them. Two definitions at the top of the cone file are never used ([SecondKernelCoupled.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/KTypeLemma/SecondKernelCoupled.lean#L20)). The discrete series hypothesis and the notion of a $K$-type have more than one copy in the development, and the supertrace theorem uses the copies of the general notation. The measure $dk$ is the Haar measure on $K_\varepsilon$ of that notation, without normalization; both sides use it. We opened the statements of the layer lemma, the pointwise supertrace identity, the reduction from $Y$ to $Y_0$, the reduction to the kernel and the $K$-type lemma ([SupTrace.lean](lean:ReciprocityTheory/ReductiveGroups/DiscreteSeries/TraceGap/SupTrace.lean#L75)), but not their proofs. In the cone theorem we did not open the lemmas that build the auxiliary module and its weight bound, and in the kernel theorem we did not open the construction of $z$ or the uniqueness lemma.
