---
title: Transfer operators and the cost of derivatives
decls:
  - qnHermHaar
  - qnTInv
  - operator_word_cost
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Transfer operators and the cost of derivatives

This section collects three analytic facts about differential operators on a unitary group of signature $(m - 1, 1)$. The first two concern the transfer matrix of quantum minors: it is Hermitian for the $L^2$ pairing of a Haar measure, and it commutes with translation by the stabilizers of the data. The third bounds the derivatives of a function along a family of slices by its derivatives along words in the Lie algebra, with an explicit loss in the power of the norm. The first is used in the theorem on the Haar invariance of the Hermitian pairing. The third is used in the theorem on the bound on derivative costs. For unitary groups see [unitary groups](/learn/groups/#unitary-groups).

### The group and the transfer matrix

We use the notation of the section on [transfer operators on a unitary group](/entry/qn-herm-haar-of-alg/). Fix $k, r \geq 0$ and put $m = 2r + k + 1$. Let $H = H_{k,r}$ be the Hermitian matrix of signature $(m - 1, 1)$ defined there, and $U(H)$ its unitary group. For $0 \leq i \leq r$, $G_i \subseteq U(H)$ is the subgroup that fixes the first $i$ hyperbolic pairs. $W_b$ is the set of vectors supported on the middle $k + 1$ coordinates. For $z \in W_b$, $S_i(z) = U_W(z) N_i$ is the product of the stabilizer of $z$ in the unitary group of $W$ and the unipotent group $N_i$.

The operators $\mathcal{E}_{ab}$ are the complexified right derivatives along the Lie algebra of $U(H)$. The transfer matrix $T(Y) = (T_{pq}(Y))_{p, q \in \{0, 1\}}$ is the $2 \times 2$ matrix of operators built from quantum minors of the $\mathcal{E}_{ab}$ at the shift $u(Y) = Y + (m_i - 1)/2$, contracted with the coordinates of $z$ and $z'$. It depends on $z, z' \in W_b$ and on $i$.

### Hermitian symmetry and invariance

**Theorem 4.4.1 (Hermitian symmetry of the transfer matrix).** Let $k, r \geq 0$, $z, z' \in W_b$, $0 \leq i \leq r$, and let $\mu$ be a Haar measure on $G_i$. Let $f_1$ and $f_2$ be complex functions that are smooth on $G_i$ and have compact support in $G_i$. Then for all $Y \in \mathbb{C}$ and $p, q \in \{0, 1\}$,
$$\int_{G_i} T_{pq}(Y) f_1 \cdot \overline{f_2} \, d\mu = \int_{G_i} f_1 \cdot \overline{T_{qp}(\bar Y) f_2} \, d\mu.$$

Lean: `qnHermHaar`.

*Proof.* This is [Hermitian symmetry of the transfer matrix](/entry/qn-herm-haar-of-alg/) applied to its inputs, which are all proved. The inputs are the six identities for the operators $\mathcal{E}_{ab}$ of that section and the star identity for the transfer matrix in an abstract $*$-algebra. In words: the real right derivatives are skew for the pairing $\int f_1 \bar f_2 \, d\mu$; quantum minors satisfy a star symmetry; the contractions that build $T(Y)$ are unchanged under a change of basis that also moves the vectors; two exchange relations move the vectors $y$ and $\bar y$ past a quantum minor; the Leibniz rules for $\mathcal{E}_{ab}$ against $y_c$ and $\bar y_c$ hold; and the $\mathcal{E}_{ab}$ satisfy the relations of $\mathfrak{gl}$ and preserve smoothness on $G_i$. With these inputs, the cited theorem gives the identity. $\square$

**Theorem 4.4.2 (Invariance of the transfer matrix).** Let $E$ be a complex normed space, $k, r \geq 0$, $z, z' \in W_b$ and $0 \leq i \leq r$. Let $D$ be an open set of matrices with $s g s' \in D$ for all $g \in G_i \cap D$, $s \in S_i(z)$ and $s' \in S_i(z')$, and let $f$ be an $E$-valued function that is smooth on $G_i \cap D$. Then for all $Y \in \mathbb{C}$, $p, q \in \{0, 1\}$, $s \in S_i(z)$, $s' \in S_i(z')$ and $g \in G_i \cap D$,
$$T_{pq}(Y)\big[x \mapsto f(s x s')\big](g) = \big(T_{pq}(Y) f\big)(s g s').$$

Lean: `qnTInv`.

*Proof.* This is [invariance of the transfer matrix](/entry/qn-tinv-of/) applied to proved inputs: identity 3 of that section, on the covariance of the contractions under a change of basis; identity 6, in two parts, on the relations of $\mathfrak{gl}$ and the preservation of smoothness; and the fact that quantum minors of the $\mathcal{E}_{ab}$ commute with left translations. $\square$

The invariance says that $T(Y)$ descends to functions on the double coset space $S_i(z) \backslash G_i / S_i(z')$. The symmetry says that, on this space, the adjoint of $T_{pq}(Y)$ is $T_{qp}(\bar Y)$.

### The cost of derivatives along slices

Now let $U_r = U(H_{k,r})$ and write $\mathfrak{u}_r$ for its Lie algebra. For $X \in \mathfrak{u}_r$ let $L_X$ and $R_X$ be the left and right derivatives along $X$. For words $u = (X_1, \dots, X_a)$ and $v = (X'_1, \dots, X'_b)$ put
$$D_{u,v} f = L_{X_1} \cdots L_{X_a} R_{X'_1} \cdots R_{X'_b} f.$$
A word is a *unit word* if each letter lies in $\mathfrak{u}_r$ and has all entries of absolute value at most $1$. Let $\|g\|$ be the Hilbert-Schmidt norm of a matrix.

Fix $k, p, s, \rho$ with $s \geq 1$, and put $j = p + s$, so that $U_{j + \rho}$ contains $U_\rho$ in its middle block. For $g \in U_{j+\rho}$ let $\Delta_j(g)$ be the determinant of the $j \times j$ block of $g$ in the last $j$ rows and the first $j$ columns, with the rows in reverse order.

**Definition 4.4.3 (Star bounds).** Let $E$ be a complex normed space, $F_1 : U_{j+\rho} \to E$, $A_1, B_1 \in \mathbb{R}$, $Q \in \mathbb{N}$ and $K \subseteq \mathbb{R}$. Then $F_1$ satisfies the *star bounds* $(A_1, Q, B_1, K)$ if

1. $F_1$ is $Q$ times continuously differentiable on $U_{j+\rho}$;
2. $|\Delta_j(g)| \in K$ whenever $F_1(g) \neq 0$;
3. $\|g\|^{A_1} \|D_{u,v} F_1(g)\| \leq B_1$ for all $g \in U_{j+\rho}$ and all unit words $u, v$ in the parabolic subalgebra, with $|u| + |v| \leq Q$.

Here the *parabolic subalgebra* is the set of $X \in \mathfrak{u}_{j+\rho}$ with $X_{ib} = 0$ for $b < j \leq i$.

Let $\sigma$ be a permutation of $\{0, \dots, p-1\}$ and $d \in (\mathbb{C}^\times)^p$. There is a space $\Xi$ of slice coordinates $\xi$ and, for $\xi \in \Xi$, an invertible $s \times s$ matrix $Z$ and $\gamma \in U_\rho$, a point
$$g_\xi(Z, \gamma) = R(\xi_1)^{-1}\, m(Z_\xi(Z), \gamma)\, R(\xi_2) \in U_{j+\rho}.$$
Here $R(\xi_1)$ and $R(\xi_2)$ lie in the unipotent radical of the parabolic subgroup of $U_{j+\rho}$ with Levi part $\mathrm{GL}_j \times U_\rho$, $m$ is the embedding of that Levi part, and $Z_\xi(Z)$ is a $j \times j$ matrix built from $Z$, $\sigma$, $d$ and the rest of $\xi$. We did not unfold this construction further.

**Definition 4.4.4 (Derivative cost bound).** The *derivative cost bound* is the statement: for all $k, p, s, \rho$ with $s \geq 1$, every $\sigma$ and $d$ as above, every compact $K \subseteq (0, \infty)$ and every $Q \in \mathbb{N}$, there is $C$ with this property. For every complex normed space $E$ and every $F_1$ that satisfies the star bounds $(A_1, Q, B_1, K)$, for every $\xi \in \Xi$, all unit words $u, v$ in $\mathfrak{u}_\rho$, every $q$ with $q + |u| + |v| \leq Q$, every invertible $Z$ and every $\gamma \in U_\rho$, the function
$$\Phi(Z') = D_{u,v}\big[\gamma' \mapsto F_1(g_\xi(Z', \gamma'))\big](\gamma)$$
is $q$ times differentiable at $Z$, and its $q$-th derivative satisfies
$$\|\Phi^{(q)}(Z)\| \leq C\, B_1\, \|g_\xi(Z, \gamma)\|^{-A_1 + 5 (j + \rho) q + 2 (j + \rho)(|u| + |v|)}.$$

**Theorem 4.4.5 (Derivative cost from slice components).** Assume seven statements on the slice coordinates: that the slices lie in the group, the parametrization of the unipotent radical, the right slice, the left slice, the slice in $Z$, that the directions lie in the parabolic subalgebra, and the sizes of the slice coordinates. Then the derivative cost bound holds.

Lean: `operator_word_cost`.

*Proof.* This is an assembly lemma for the derivative cost applied to seven proved lemmas. For a matrix $X$ let $\ell(X)$ be the maximum of $1$ and the largest absolute value of an entry of $X$. The lemmas say the following.

1. *Words.* Given the left and right slice statements, the derivative $D_{u,v}$ of $\gamma' \mapsto F(g_\xi(Z, \gamma'))$ is the derivative of $F$ along the words $u$ and $v$ conjugated by $R(\xi_1)$ and $R(\xi_2)$, evaluated at $g_\xi(Z, \gamma')$.
2. *Letter size.* There is $C$ such that the conjugate by $R(x)$ of a letter with entries of absolute value at most $1$ has $\ell \leq C \|R(x)\|^2$.
3. *Scaling.* Under the star bounds, $\|g\|^{A_1} \|D_{u,v} F_1(g)\| \leq B_1 \prod \ell(X)$ for all words $u, v$ in the parabolic subalgebra with $|u| + |v| \leq Q$, the product taken over all letters $X$ of $u$ and $v$.
4. *Commutation.* For $f$ that is $m$ times continuously differentiable and words $u, v, w$ in the Lie algebra of total length at most $m$, $R_w D_{u,v} f = D_{u, wv} f$ on the group.
5. *Off the support.* If $F$ vanishes on an open set that contains $g_\xi(Z, \gamma)$, then all derivatives in $Z$ of $F(g_\xi(Z, \gamma))$ vanish at $Z$.
6. *Smoothness in $Z$.* The point $g_\xi(Z, \gamma)$ lies in the group and is continuous in $Z$, and $Z \mapsto F(g_\xi(Z, \gamma))$ is $m$ times differentiable when $F$ is.
7. *Cost in $Z$.* When $|\Delta_j(g_\xi(Z, \gamma))| \in K$, the derivatives in $Z$ of $F(g_\xi(Z, \gamma))$ up to order $q$ are bounded through the bounds on the right derivatives of $F$ along words in the parabolic subalgebra at $g_\xi(Z, \gamma)$. This lemma is itself proved from lemma 6, from a formula that writes the first derivative in $Z$ as a combination of right derivatives along explicit directions, with coefficients from the entries of $Z^{-1} W$, and from a bound on the size of these directions.

The assembly combines them in this order: lemma 1 moves the derivatives onto $F_1$, lemmas 2 and 3 bound the conjugated words, lemma 4 merges the right derivatives from $Z$ with the word $v$, and lemmas 5 to 7 bound the derivatives in $Z$. $\square$

**Remark 4.4.6 (Formalization).** The derivative cost theorem is an implication. Its seven hypotheses on the slices are not discharged by it; its caller has to supply them. See [UsCost.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/UsCost.lean#L13) and the statement in [StatementU.lean](lean:Formalism/HermitianCurvature/StatementU.lean#L298). The seven slice statements and the construction of $g_\xi$ were not unfolded beyond what the text says. Lemma 7 was read only up to its hypotheses; the form of its bound and the way the exponent of the conclusion arises were not checked. The symmetry and invariance theorems take all their inputs from proved lemmas, so they hold without hypotheses; see [QnHermHaar.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/QnHermHaar.lean#L14) and [QnTInv.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/QnTInv.lean#L10). Their statements are in [StatementQ.lean](lean:Formalism/HermitianCurvature/StatementQ.lean#L543) and [StatementQ.lean](lean:Formalism/HermitianCurvature/StatementQ.lean#L347).
