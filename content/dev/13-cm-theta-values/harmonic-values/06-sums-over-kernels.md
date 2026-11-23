---
title: Sums of harmonic values over kernels of similitudes
decls:
  - GlobalTheory.PlaceInt.FormSum.sum_hv_formal_kernel
  - GlobalTheory.T.sum_harmonicValues_formalKernel_similitude
  - GlobalTheory.sum_hv_primary_kernel
  - GlobalTheory.T.sum_hv_primary_kernel_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Sums of harmonic values over kernels of similitudes

At a finite place, the step [every character of literature](/step/every-character-of-literature/) needs a lower bound for the valuation of a sum of harmonic values. The sum runs over the translates of a family of sections by the points of the kernel of a similitude $pq$. This section proves that such a sum is the number of points of $\ker q$, times a determinant of $p$, times an element of controlled valuation. The proof is a trace formula on the formal group of an integral chart. It uses the translation units of the [previous section](/entry/exists-tr-unit/) and a splitting of the formal kernel. The background is in [formal group laws](/learn/formal-groups/#formal-group-laws), [height](/learn/formal-groups/#height) and [abelian schemes](/learn/abelian-varieties/#abelian-schemes).

### Setting

Let $E$ be a CM [[number field|MWBDFS2KJ5]] and assume that the involution of $\mathcal{O}_E$ is the conjugation of $E$. Let $T$ be a complete [[discrete valuation ring|MGM3CNJW9V]] of characteristic $0$ with normalized valuation $v$, and let $F \to \operatorname{Frac} T$ be an embedding of the coefficient field. Let $y$ be an integral framed point with abelian variety $A_x$, and let $C$ be an integral chart at $y$. We assume that $C$ is *good*: its frames are compatible with truncation and its formal group has a uniformization with a torsion isomorphism. We do not unfold this condition. Let $\nabla$ be a canonical connection.

For sections $s_1, \dots, s_n$ of $L^k$ and a polynomial $P$ in the letters, the harmonic value is
$$\mathrm{hv}(s, P) = \sum_m P_m \prod_{b=1}^n \nabla_y(s_b)(m_b),$$
as in the [third section](/entry/harm-nab-eq-poly-deriv/).

**Definition 2.6.1 (chart bound).** Let $e > 0$ and $\rho \in \mathbb{R}$. The chart $C$ satisfies the *chart bound* $(e, \rho)$ for row degree $a$ and $n$ columns if, for every level $k$, the infimum of $v(z)/e$ over the chart values $z$ of level $k$ of integral series under integral harmonic polynomials of degree $a$ is at least $-\rho$. We do not unfold the infimum further.

**Definition 2.6.2 (similitude and kernel).** An $n \times n$ matrix $\mu$ over $\mathcal{O}_E$ is a *similitude* of factor $N$ if $\mu^\ast \mu = N \cdot 1$, where $\mu^\ast$ is the conjugate transpose. An $n$-tuple $u$ of points of $A_x$ is *killed* by $\mu$ if $\sum_j \mu_{ij} u_j = 0$ for every $i$.

For a matrix $\gamma$ over $E$, let $P^\gamma$ be the image of $P$ under the substitution $X_{\tau, i, j} \mapsto \sum_b \tau(\gamma_{bj}) X_{\tau, i, b}$. For a matrix $x$ over $\mathcal{O}_E$, put $\det_m(x) = \prod_\tau \tau(\det x)^{m_\tau}$.

### The trace formula on the formal group

**Theorem 2.6.3 (sum over the formal kernel).** Let $C$ be good with chart bound $(e, \rho)$ for $a$ and $n$, with $e > 0$. Let $\ell$ be a prime that is not a unit in $T$. Let $N$ be odd, and let $p, q$ be matrices over $\mathcal{O}_E$ such that $pq$ is a similitude of factor $N^2$. Let $N^2 = kM$ with $k$ prime to $\ell$, and assume that all $M$-torsion points of $A_x$ are rational. Let $(a_i)_{i \in J}$ be an injective family that runs over the $n$-tuples killed by $pq$ whose coordinates are formal points of $C$. Let $s_1, \dots, s_n$ be regular sections of $L^{N^2}$, and let $G_{i,b}$ be the symmetric translate of $s_b$ by $a_{i,b}$. Assume that for every $i$ with $q a_i = 0$ there are $r_b \in T$ with $\prod_b r_b = 1$ and $G_{i,b} = r_b s_b$. Let $P \in \mathcal{H}_a$ and $c \in F$, and assume that $c\, P^{pq}$ is integral of level $1$. Then there is $z \in \operatorname{Frac} T$ with $v(z)/e \geq -\rho$ and
$$c \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q a_i = 0\} \cdot \det_m(p) \cdot z.$$

Lean: `GlobalTheory.PlaceInt.FormSum.sum_hv_formal_kernel` (also `GlobalTheory.T.sum_harmonicValues_formalKernel_similitude`, a second name).

*Proof.* Let $B$ be the integral formal data of $C$. Under the chart bound, every value of level $1$ of an integral series under an integral polynomial has $v/e \geq -\rho$.

*Step 1: germs and points.* Each $s_b$ has an integral germ $f_b$. Put $f = \prod_b f_b$ on $n$ copies of the formal group. Each $a_i$ has formal coordinates $\alpha_i$, and $i \mapsto \alpha_i$ is a bijection from $J$ onto the kernel of $pq$ acting on $n$ copies of the formal group.

*Step 2: translates.* By the [theorem on translation units](/entry/exists-tr-unit/) there are units $u_{i,b}$ such that the germ of $G_{i,b}$ is $u_{i,b} \cdot \mathrm{sh}_{\alpha_{i,b}} f_b$. Put $U_i = \prod_b u_{i,b}$.

*Step 3: the factor $\kappa$.* There is an integral series $\kappa$ with constant term $1$ that is the exponential of the gauge along the similitude. The laws of the translation units give $U_i \cdot \mathrm{sh}_{\alpha_i} \kappa = \kappa$ for every $i$.

*Step 4: the trace.* The formal group has finite height, its kernel splits because $\ell$ is not a unit and the $M$-torsion is rational, and the Jacobian of $pq$ is not zero. Under these conditions, a series invariant under the shifts by the kernel of $q$ has a trace over the kernel of $pq$ equal to $\#\ker q \cdot \mathrm{jac}(p)$ times the pullback along $pq$ of an integral series $g$. For $q a_i = 0$, the hypothesis $G_i = r s$ gives $U_i \cdot \mathrm{sh}_{\alpha_i} f = f$. A twisted form of the trace then gives
$$\sum_{i \in J} U_i \cdot \mathrm{sh}_{\alpha_i} f = \#\ker q \cdot \mathrm{jac}(p) \cdot \kappa \cdot (pq)^\ast g.$$

*Step 5: Jacobians.* The Jacobian of $x$ on the formal group is $\det_m(x)$. For $x = pq$ it is not zero, since $\det\bigl((pq)^\ast\bigr) \det(pq) = N^{2n} \neq 0$.

*Step 6: values.* The harmonic value $\mathrm{hv}(G_i, P)$ is the chart value of level $N^2$ of $U_i \cdot \mathrm{sh}_{\alpha_i} f$ under $P$, and this value is linear in the series. On $\kappa \cdot (pq)^\ast g$, the value of level $N^2$ under $P$ is the value of level $1$ of $g$ under $P^{pq}$. Let $z$ be the value of level $1$ of $g$ under $c P^{pq}$. The bound of the first paragraph gives $v(z)/e \geq -\rho$. $\square$

### The primary part of the kernel

The second theorem removes the condition that the points lie in the formal group. It allows all points of $\ell$-power order and uses the cosets of the formal kernel.

**Theorem 2.6.4 (sum over the primary kernel).** Keep the setting of the previous Theorem up to the factorization $N^2 = kM$. Let $g$ be a matrix over $\mathcal{O}_E$ with $g q = k_1 N$ and $k_1$ prime to $\ell$. Let $(a_i)_{i \in J}$ be an injective family that runs over the $n$-tuples killed by $pq$ whose coordinates have $\ell$-power order. Assume that the Weil pairings of level $N^2$ between the $a_i$ have product $1$, in a form that we do not unfold. Let $s_1, \dots, s_n$ be sections of $L^{N^2}$ that are reached from the frame section by norm pulls and moves, and that are fixed by every point $u$ of $\ell$-power order with $N u = 0$. Let $G_{i,b}$ be the symmetric translate of $s_b$ by $a_{i,b}$. Let $P \in \mathcal{H}_a$ and $c \in F$ with $c\, P^{pq}$ integral of level $1$. Then there is $z \in \operatorname{Frac} T$ with $v(z)/e \geq -\rho$ and
$$c \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q a_i = 0\} \cdot \det_m(p) \cdot z.$$

Lean: `GlobalTheory.sum_hv_primary_kernel` (also `GlobalTheory.T.sum_hv_primary_kernel_alt`, a second name).

*Proof.* Let $W$ be the image of $a$, let $W_0 = W \cap \ker q$, and let $W_1$ be the set of elements of $W$ whose coordinates are formal points of $C$.

*Step 1: $W_0$ does not change the harmonic value.* Let $u \in W_0$. From $g q = k_1 N$ and $k_1$ prime to $\ell$ we get $N u = 0$, so $u$ fixes each $s_b$. With the Weil pairing hypothesis and $N$ odd, translation by $u$ multiplies the translates by scalars with product $1$. Since the harmonic value is multilinear in the sections, it does not change.

*Step 2: cosets.* A lemma on finite abelian groups writes the sum over $W$ as $\# W_0$ times a sum of sums over cosets of $W_1$. The set $\{z : v(z)/e \geq -\rho\}$ is closed under sums.

*Step 3: one coset.* On each coset, apply the Theorem on the formal kernel. Its hypotheses come from three facts: rational torsion splits the kernel, a tuple is killed on formal points exactly when its coordinates lie in the coordinate kernel, and a reached section is regular on the integral model. Step 1 gives the condition on $\ker q$. $\square$

**Remark 2.6.5.** The factor $\#\ker q \cdot \det_m(p)$ is the analogue of the classical formula for the trace of a separable isogeny on functions: summing translates over the kernel of an isogeny $\varphi$ gives $\deg \varphi$ times a pullback along $\varphi$, up to the Jacobian. Here the isogeny is a similitude, and the Jacobian of $p$ is a product of embedded determinants. For the formal theory of isogenies and height, see Silverman, *The Arithmetic of Elliptic Curves*, Chapter IV, for dimension $1$.

**Remark 2.6.6 (Formalization).** The trace formula is in [SumHarmonicValuesFormalKernelSimilitude.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHarmonicValuesFormalKernelSimilitude.lean#L203), and its second name in [SumHarmonicValuesFormalKernelSimilitudeStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHarmonicValuesFormalKernelSimilitudeStatement.lean#L11). The primary version is in [SumHvPrimaryKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHvPrimaryKernel.lean#L221), and its second name in [SumHvPrimaryKernelStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHvPrimaryKernelStatement.lean#L11). Both second names are proved by `first` combinators. The harmonic value, the reach relation, the chart bound and the formal points are in [AdaptStd.lean](lean:Development/AbelianVarietyTheory/Definitions/PlaceAdaptation/AdaptStd.lean#L98). The chart bound enters only through the bound on values of the integral formal data, and it is close to the definition of that bound.
