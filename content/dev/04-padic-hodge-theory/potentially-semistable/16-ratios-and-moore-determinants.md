---
title: Ratios of Frobenius eigenvectors and the Moore determinant
decls:
  - GlobalTheory.T.crisPlus_frob_eigenvector_ratio_padic
  - GlobalTheory.PMon.ratio_holds
  - GlobalTheory.PMon.RatioTransport.ratio_of_acris
  - GlobalTheory.PMon.RatioTransport.ratio_integral
  - GlobalTheory.T.mooreDeterminant_crisPlus_ne_zero
  - GlobalTheory.PMon.moore_statement
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Ratios of Frobenius eigenvectors and the Moore determinant

This section and the five after it prove the matrix form of the monodromy theorem, to which [the p-adic monodromy theorem](/entry/de-rham-potentially-semistable/) was reduced in the previous section. The proof is an induction on weights. Its main step, [the weight modification](/entry/monodromy-irreducible-elementary-weight-modification/), rests on a lemma about lattices, and that lemma needs eigenvectors of a power of Frobenius in $B_{\mathrm{cris}}^+$. Here we prove two facts about such eigenvectors. First, if two eigenvectors of $\varphi^h$ with the same eigenvalue $\ell^s$, $s < h$, have a quotient that is fixed by $\varphi$, then the quotient is a constant in $\mathbb{Q}_\ell$. Second, as a consequence, the Moore determinant of linearly independent eigenvectors with eigenvalue $\ell$ is not zero. The second fact is used in [the lattice lemma in degree one](/entry/fundamental-lemma-lattice-degree-one/) and in [the construction of vectors of the second kind](/entry/exists-second-kind-matrix-moore-det-ne-zero/).

We keep the notation of the previous section: a prime $\ell$, local period data at $\ell$ tied to their $A_{\inf}$ data, the rings $B$ and $B_{\mathrm{dR}}$, the map $\iota : B \to B_{\mathrm{dR}}$, the filtration $\mathrm{Fil}^\bullet$ of $B_{\mathrm{dR}}$, and the unit $t_B$ of $B$. Let $\varphi : B \to B$ be the Frobenius. For $a \in \mathbb{Z}$ write $t^a = \iota(t_B^a)$; so $t = t^1 = \iota(t_B)$. The tie gives a ring isomorphism $e_B : B \to B_{\mathrm{cris}}$ that commutes with Frobenius and is the identity on $\mathbb{Z}_\ell$. Fontaine's ring $A_{\mathrm{cris}}$ maps to $B_{\mathrm{cris}}$. Maps such as $\varphi$ and $\iota$ act on vectors and matrices entry by entry.

We use the following facts about these rings. They are proved elsewhere in this development.

1. $B_{\mathrm{dR}}$ is a field and $\iota$ is injective. So $B$ is an integral domain.
2. $\mathrm{Fil}^a \cdot \mathrm{Fil}^b \subseteq \mathrm{Fil}^{a+b}$. For $a, b \in \mathbb{Z}$, $x \in \mathrm{Fil}^a$ if and only if $t^b x \in \mathrm{Fil}^{a+b}$. Every $x \neq 0$ has an exact degree: there is $a$ with $x \in \mathrm{Fil}^a$ and $x \notin \mathrm{Fil}^{a+1}$. Every $x \in \mathrm{Fil}^0 \setminus \mathrm{Fil}^1$ is a unit, and $x^{-1} \in \mathrm{Fil}^0$. Also $t^{a+b} = t^a t^b$ and $t^0 = 1$.
3. The map $A_{\mathrm{cris}} \to B_{\mathrm{cris}}$ is injective, commutes with Frobenius, and is the identity on $\mathbb{Z}_\ell$.

**Definition 6.16.1 (Positive elements).** An element $b \in B$ is *positive* if there are $N \geq 0$ and $x \in A_{\mathrm{cris}}$ such that $e_B(\ell^N b)$ is the image of $x$ in $B_{\mathrm{cris}}$. Let $B^+$ be the set of positive elements.

Lean: `GlobalTheory.PMon.Plus`.

Under $e_B$, the set $B^+$ is the image of $A_{\mathrm{cris}}[1/\ell]$, which is Fontaine's ring $B_{\mathrm{cris}}^+$. We use these properties of $B^+$, proved elsewhere in this development: $B^+$ is closed under sums and products and stable under $\varphi$; it contains $\mathbb{Q}_\ell$, the image of $A_{\inf}$ and $t_B$; and $\iota(\varphi^j b) \in \mathrm{Fil}^0$ for every $b \in B^+$ and every $j \geq 0$.

**Definition 6.16.2 (Moore matrix).** Let $k \geq 0$ and $a = (a_0, \dots, a_{k-1}) \in B^k$. The *Moore matrix* of $a$ is the $k \times k$ matrix
$$M(a) = \big(\varphi^i(a_j)\big)_{0 \leq i, j < k}.$$

Over a finite field with $q$ elements, the matrix $(a_j^{q^i})$ has the same form, and its determinant is not zero exactly when the $a_j$ are linearly independent over the prime field. The theorem at the end of this section is an analogue for eigenvectors of Frobenius in $B^+$.

**Lemma 6.16.3 (Ratio of integral eigenvectors).** Let $s < h$. Let $b, b' \in B$, and let $y, y' \in A_{\mathrm{cris}}$ be such that $e_B(b)$ and $e_B(b')$ are the images of $y$ and $y'$. Assume
$$\varphi^h(b) = \ell^s b, \qquad \varphi^h(b') = \ell^s b', \qquad b' \neq 0, \qquad \varphi(b)\, b' = b\, \varphi(b').$$
Then there is $c \in \mathbb{Q}_\ell$ with $b = c\, b'$.

Lean: `GlobalTheory.PMon.RatioTransport.ratio_integral`.

*Proof.* We move the problem to $A_{\mathrm{cris}}$. The map $e_B$ is a ring isomorphism that commutes with $\varphi$, and $A_{\mathrm{cris}} \to B_{\mathrm{cris}}$ is an injective ring map that commutes with $\varphi$ (fact 3). So the images of $\varphi^h(y) - \ell^s y$ and of $\varphi(y) y' - y \varphi(y')$ in $B_{\mathrm{cris}}$ are $e_B(\varphi^h(b) - \ell^s b) = 0$ and $e_B(\varphi(b) b' - b \varphi(b')) = 0$. By injectivity,
$$\varphi^h(y) = \ell^s y, \qquad \varphi^h(y') = \ell^s y', \qquad \varphi(y)\, y' = y\, \varphi(y').$$
In the same way $y' \neq 0$, since $b' \neq 0$ and $e_B$ is injective. Now we apply the corresponding statement in $A_{\mathrm{cris}}$, [Theorem 6.22.3](/entry/ratio-proportional-target/): for $s < h$ and $w, w' \in A_{\mathrm{cris}}$ with these three relations and $w' \neq 0$, there are $c, d \in \mathbb{Z}_\ell$ with $c \neq 0$ and $c\, w = d\, w'$. This gives $c, d$ with $c\, y = d\, y'$. Apply the map to $B_{\mathrm{cris}}$ and then $e_B^{-1}$. Both maps are the identity on $\mathbb{Z}_\ell$, so $c\, b = d\, b'$ in $B$. Since $c \neq 0$ and $B$ is a $\mathbb{Q}_\ell$-algebra, $b = (d/c)\, b'$. $\square$

**Theorem 6.16.4 (Ratio of Frobenius eigenvectors).** Let $s < h$. Let $\omega, \omega' \in B^+$ with
$$\varphi^h(\omega) = \ell^s \omega, \qquad \varphi^h(\omega') = \ell^s \omega', \qquad \omega' \neq 0, \qquad \varphi(\omega)\, \omega' = \omega\, \varphi(\omega').$$
Then there is $c \in \mathbb{Q}_\ell$ with $\omega = c\, \omega'$.

Lean: `GlobalTheory.T.crisPlus_frob_eigenvector_ratio_padic` (also `GlobalTheory.PMon.ratio_holds` and `GlobalTheory.PMon.RatioTransport.ratio_of_acris`, second names).

The last relation says that the quotient $\omega/\omega'$, in the fraction field of the domain $B$, is fixed by $\varphi$. The theorem says that such a quotient is a constant.

*Proof.* Since $\omega$ and $\omega'$ are positive, there are $N, M \geq 0$ and $x, x' \in A_{\mathrm{cris}}$ such that $e_B(\ell^N \omega)$ is the image of $x$ and $e_B(\ell^M \omega')$ is the image of $x'$. Put $u = \ell^{N+M}$, $b = u\omega$ and $b' = u\omega'$. Then $e_B(b)$ is the image of $\ell^M x$, and $e_B(b')$ is the image of $\ell^N x'$. Since $\varphi$ fixes $u$, we have $\varphi^h(b) = \ell^s b$ and $\varphi^h(b') = \ell^s b'$. Since $u$ is a unit of $B$, $b' \neq 0$. Multiplication of the last relation by $u^2$ gives $\varphi(b) b' = b \varphi(b')$. The [Lemma 6.16.3](/entry/ratio-integral/) gives $c \in \mathbb{Q}_\ell$ with $u\omega = c\, u\omega'$. Cancel the unit $u$. $\square$

**Theorem 6.16.5 (Moore determinant).** Let $k \leq h$. Let $a = (a_0, \dots, a_{k-1})$ be a family of elements of $B^+$ such that $\varphi^h(a_j) = \ell\, a_j$ for every $j$, and such that the $a_j$ are linearly independent over $\mathbb{Q}_\ell$. Then $\det M(a) \neq 0$.

Lean: `GlobalTheory.T.mooreDeterminant_crisPlus_ne_zero` (also `GlobalTheory.PMon.moore_statement`, a second name).

*Proof.* By fact 1, $B$ is an integral domain. If $k = 0$, the determinant of the empty matrix is $1$. For $k \geq 1$ we prove the claim by induction on $k$, for all families of size $k \leq h$.

For $k = 1$, $\det M(a) = a_0$, which is not zero since a family of one element that is linearly independent has a nonzero element.

Let $k = n + 1$ with $n \geq 1$, and assume the claim for families of size $n$. Suppose $\det M(a) = 0$; we derive a contradiction. Let $M = M(a)$, with rows and columns indexed by $0, \dots, n$. For $0 \leq m \leq n$, let $\omega_m$ be the determinant of the $n \times n$ matrix $(\varphi^i(a_j))$ with $0 \leq i < n$ and $j \neq m$. This is the Moore matrix of the family $a$ with $a_m$ removed, and $\omega_n = \det M(a_0, \dots, a_{n-1})$. The family $a_0, \dots, a_{n-1}$ is linearly independent and has size $n \leq h$, so $\omega_n \neq 0$ by induction.

Let $\operatorname{adj} M$ be the adjugate matrix. Its entries in the last column are cofactors for the last row of $M$: $(\operatorname{adj} M)_{m, n} = (-1)^{n+m}\omega_m$. Its entries in the first column are cofactors for the row $0$; the minor is the determinant of the rows $1, \dots, n$, which are $\varphi$ applied to the rows $0, \dots, n-1$. So $(\operatorname{adj} M)_{m, 0} = (-1)^m \varphi(\omega_m)$. Since $M \operatorname{adj} M = \det(M) \cdot 1 = 0$, every column of $\operatorname{adj} M$ lies in the kernel of $M$. So the vector
$$v = (\operatorname{adj} M)_{n,n} \cdot (\operatorname{adj} M)_{\bullet, 0} - (\operatorname{adj} M)_{n,0} \cdot (\operatorname{adj} M)_{\bullet, n}$$
lies in the kernel of $M$, and its last entry is $0$. The first $n$ rows of $M v = 0$ then say that $M(a_0, \dots, a_{n-1})$ kills the first $n$ entries of $v$. That matrix has determinant $\omega_n \neq 0$, so all entries of $v$ vanish. After the signs are removed, $v_m = 0$ reads
$$\varphi(\omega_m)\, \omega_n = \omega_m\, \varphi(\omega_n) \quad \text{for every } m.$$

Each $\omega_m$ lies in $B^+$, since $B^+$ is a ring that is stable under $\varphi$. Each column of the matrix of $\omega_m$ is multiplied by $\ell$ under $\varphi^h$, because $\varphi^h$ commutes with $\varphi^i$ and fixes $\ell$. So $\varphi^h(\omega_m) = \ell^n \omega_m$. Here $n < n + 1 \leq h$. The [Theorem 6.16.4](/entry/cris-plus-frob-eigenvector-ratio-padic/) on ratios, with $s = n$ and $\omega' = \omega_n$, gives $c_m \in \mathbb{Q}_\ell$ with $\omega_m = c_m \omega_n$.

Now take the row $0$ of $M \operatorname{adj} M = 0$ against the last column of $\operatorname{adj} M$:
$$0 = \sum_{m=0}^{n} a_m (-1)^{n+m} \omega_m = \Big( \sum_{m=0}^{n} (-1)^{n+m} c_m\, a_m \Big)\, \omega_n.$$
Since $B$ is a domain and $\omega_n \neq 0$, the sum in parentheses is $0$. By linear independence, $c_n = 0$. But $\omega_n = c_n \omega_n$, so $\omega_n = 0$, a contradiction. $\square$

**Remark 6.16.6 (Formalization).** The names under `GlobalTheory.T` are `first | exact ...` wrappers under `maxHeartbeats 1000000`. The proof of `GlobalTheory.PMon.ratio_holds` is the term `RatioTransport.ratio_of_acris` ([CrisPlusFrobEigenvectorRatioPadic.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrisPlusFrobEigenvectorRatioPadic.lean#L12)). Positivity is the predicate `Plus` in [AdmSt.lean](lean:Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/AdmSt.lean#L70); it is not a subring by definition, and its ring properties come from `GlobalTheory.T.bcrisPlus_frobeniusStable_subring_in_filZero`. Facts 1 and 2 are clauses of `GlobalTheory.T.deRhamPeriodRing_field_tPow_filtration_units`, and fact 3 is `GlobalTheory.PMon.Trans.acris_bcris`. The induction of the Moore theorem is the lemma `GlobalTheory.PMon.MooreDeterminant.moore_core` ([MooreDeterminantCrisPlusNeZero.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MooreDeterminantCrisPlusNeZero.lean#L32)), stated for any domain that is an algebra over a field, with a subset closed under the ring operations and $\varphi$ and with a $\varphi$-fixed element $L$ in place of $\ell$. The case $k = 0$ is treated separately at [line 161](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/MooreDeterminantCrisPlusNeZero.lean#L161). The ratio theorem is used there only with $s = n < h$.
