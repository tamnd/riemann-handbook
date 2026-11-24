---
title: Transfer operators on a unitary group
decls:
  - PI.QnHermHaar.qnHermHaar_of_alg
  - PI.QnHermHaar.glue_holds_var
  - Formalism.FourierDecayAlt.Q.TInvW.qnTInv_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Transfer operators on a unitary group

The local computations at the real place use a $2 \times 2$ matrix of differential operators on the unitary group $U(p, q)$, built from quantum minors of the generators of its Lie algebra. Two properties of this matrix are needed. It is symmetric for the Haar measure: the adjoint of each entry is the transposed entry at the conjugate parameter. And it commutes with left and right translation by the subgroups that fix the data. This section proves both. They are the theorems on [Hermitian symmetry](/entry/qn-herm-haar/) and on [invariance](/entry/qn-tinv/) of the chapter on orbital bounds.

### The group and its level subgroups

Fix integers $k, r \geq 0$ and put $m = 2r + k + 1$. Let $H = H_{k,r}$ be the Hermitian $m \times m$ matrix with $H_{ij} = 1$ when $i + j = m - 1$ and $\min(i, j) < r$, with $H_{ii} = 1$ for $r \leq i < r + k$, with $H_{r+k, r+k} = -1$, and with all other entries $0$. Let
$$U(H) = \{ g \in M_m(\mathbb{C}) : g^* H g = H \}$$
be its [unitary group](/learn/groups/#unitary-groups), and $\langle u, v \rangle = v^* H u$ the Hermitian form, linear in the first variable. The first $r$ basis vectors $e_a$ and the last $r$ basis vectors $e^*_a$ span hyperbolic planes; the middle $k + 1$ coordinates span the space $W$. Write $W_b$ for the set of vectors supported in $W$.

For $0 \leq i \leq r$ let $G_i \subseteq U(H)$ be the subgroup that fixes $e_a$ and $e^*_a$ for all $a < i$. Let $N$ be the set of $g \in U(H)$ with $g_{ja} = \delta_{ja}$ for all $a < r$ and $j \geq a$, and with $g_{jl} = \delta_{jl}$ for all $r \leq l \leq r + k$ and $j \geq r$. So $g e_a$ is $e_a$ plus a combination of $e_0, \dots, e_{a-1}$, and $g$ moves a vector of $W$ only by a combination of $e_0, \dots, e_{r-1}$. These elements stabilize the isotropic flag $\langle e_0 \rangle \subset \langle e_0, e_1 \rangle \subset \cdots$ and act trivially on its successive quotients, as in the unipotent radical of a [parabolic subgroup](/learn/groups/#parabolic-subgroups). Put $N_i = N \cap G_i$. For $z \in W_b$ let $U_W(z)$ be the subgroup of $U(H)$ that fixes all $e_a$, all $e^*_a$, and $z$. Put $S_i(z) = U_W(z) N_i$.

### Quantum minors and the transfer matrix

The Lie algebra of $U(H)$ acts on smooth functions by right differentiation, $(R_X f)(g) = \frac{d}{dt} f(g \exp tX)|_{t=0}$. Each elementary matrix $E_{ab}$ splits as $X_1 + i X_2$ with $X_1, X_2$ in the Lie algebra of $U(H)$. Put $\mathcal{E}_{ab} = R_{X_1} + i R_{X_2}$. These operators satisfy the relations of $\mathfrak{gl}_m$:
$$[\mathcal{E}_{ab}, \mathcal{E}_{cd}] = \delta_{bc} \mathcal{E}_{ad} - \delta_{da} \mathcal{E}_{cb}.$$

**Definition 7.3.1 (Quantum minor).** Let $\mathcal{E}_{ab}$ be elements of an algebra that satisfy the relations of $\mathfrak{gl}_m$. For index sequences $a, b$ of length $t$ and $u \in \mathbb{C}$ the *quantum minor* is
$$\mathcal{E}^{a}_{b}(u) = \sum_{\pi \in S_t} \operatorname{sgn}(\pi) \prod_{j=0}^{t-1} \big( \mathcal{E}_{a_{\pi j} b_j} + (u - j) \delta_{a_{\pi j} b_j} \big),$$
the product taken in the order $j = 0, 1, \dots, t - 1$ from left to right.

For $t = m$ and $a = b$ the identity sequence this is the Capelli determinant with a shift. Now fix $i$ and let $m_i = 2(r - i) + k + 1$; we use only the indices $i, i + 1, \dots, i + m_i - 1$, which carry $G_i$. Put $u(Y) = Y + (m_i - 1)/2$. Let $f_i(z) = e_i$ if $i < r$ and $f_i(z) = z$ if $i = r$. For $g \in U(H)$ and $0 \leq j < m_i$ define
$$y_j(g) = (g^{-1} f_i(z))_{i+j}, \quad \bar y_j(g) = \langle g e_{i+j}, f_i(z) \rangle, \quad x_j = f_i(z')_{i+j}, \quad \bar x_j = \langle e_{i+j}, f_i(z') \rangle.$$
Write $\hat a$ and $\hat a \hat a'$ for the index sequence with the entries $a$, or $a$ and $a'$, removed.

**Definition 7.3.2 (Transfer matrix).** The *transfer matrix* $T(Y) = (T_{pq}(Y))_{p, q \in \{0, 1\}}$ is the matrix of operators on functions on $U(H)$ given by
$$\begin{aligned} T_{00}(Y) &= \mathcal{E}(u), \\ T_{01}(Y) &= -\sum_{a, b} (-1)^{a+b} \bar y_a x_b\, \mathcal{E}^{\hat a}_{\hat b}(u - 1), \\ T_{10}(Y) &= -\sum_{a, b} (-1)^{a+b} \bar x_a y_b\, \mathcal{E}^{\hat a}_{\hat b}(u), \\ T_{11}(Y) &= -\sum_{a < a',\, b < b'} (-1)^{a+a'+b+b'} (\bar y_a \bar x_{a'} - \bar y_{a'} \bar x_a)(y_b x_{b'} - y_{b'} x_b)\, \mathcal{E}^{\hat a \hat a'}_{\hat b \hat b'}(u - 1), \end{aligned}$$
with $u = u(Y)$, $\mathcal{E}(u)$ the full quantum minor on the $m_i$ indices, and the functions $y, \bar y$ evaluated at the point where the result is evaluated.

$T_{00}$ is a Capelli operator, and the other entries are contractions of quantum minors of size $m_i - 1$ and $m_i - 2$ with the vectors that define the data.

### Hermitian symmetry

We take the following identities as given. Each is proved elsewhere in the development.

**Theorem 7.3.3 (Identities for the operators $\mathcal{E}_{ab}$).** Let $\mu$ be a Haar measure on $G_i$.

1. For $X$ in the Lie algebra of $G_i$ and smooth compactly supported $f_1, f_2$ on $G_i$, $\int (R_X f_1) \bar f_2 \, d\mu = -\int f_1 \overline{R_X f_2} \, d\mu$.
2. In a complex $*$-algebra, if $\mathcal{E}_{ab}^* = \varepsilon_a \varepsilon_b \mathcal{E}_{ba}$ with signs $\varepsilon$, then $(\mathcal{E}^a_b(w))^* = \prod_j \varepsilon_{a_j} \varepsilon_{b_j}\, \mathcal{E}^b_a(\bar w)$.
3. The quantum determinant and the contractions above are unchanged when $\mathcal{E}$ is replaced by $P \mathcal{E} Q$ with $PQ = QP = 1$ and the vectors are moved by $Q$ and $P$.
4. Two exchange relations move a commuting family $y$ with $[\mathcal{E}_{ab}, y_c] = -\delta_{ac} y_b$ (or a family $\eta$ with $[\mathcal{E}_{ab}, \eta_c] = \delta_{bc} \eta_a$) past a quantum minor, with a shift of the parameter by $1$.
5. The Leibniz rules $\mathcal{E}_{ab}(y_c f) = y_c \mathcal{E}_{ab} f - \delta_{ac} y_b f$ and $\mathcal{E}_{ab}(\bar y_c f) = \bar y_c \mathcal{E}_{ab} f + \delta_{bc} \bar y_a f$ on $G_i$.
6. The relations of $\mathfrak{gl}_{m_i}$ for the $\mathcal{E}_{ab}$ on $G_i$, and the facts that each $\mathcal{E}_{ab}$ is linear and preserves smoothness and the left equivariance $f(ng) = \psi_z(n) f(g)$ for $n \in N_i$, where $\psi_z$ is a fixed character of $N_i$ attached to $z$.

Identity 2 is the form that the classical symmetry of quantum minors takes for a real form, and identity 4 is the exchange relation for quantum minors and vectors.

From identities 2, 3 and 4 one proves an identity in an abstract algebra.

**Lemma 7.3.4 (Star identity for the transfer matrix).** Let $A$ be a complex $*$-algebra, let $\mathcal{E}_{ab} \in A$ satisfy the relations of $\mathfrak{gl}_m$, and let $h$ be a Hermitian matrix with $h^2 = 1$ and $\mathcal{E}_{ab}^* = \sum_{c,d} h_{cb} h_{ad} \mathcal{E}_{cd}$. Let $y_c, \bar y_c \in A$ commute with each other, with $[\mathcal{E}_{ab}, y_c] = -\delta_{ac} y_b$, $[\mathcal{E}_{ab}, \bar y_c] = \delta_{bc} \bar y_a$ and $\bar y_c = \sum_l h_{lc} y_l^*$, and let $x, \bar x \in \mathbb{C}^m$ with $\bar x_c = \sum_l h_{lc} \bar{x_l}$. Define $T^A(u)$ by the formulas of the transfer matrix in $A$. Then $T^A_{pq}(u)^* = T^A_{qp}(\bar u)$.

This lemma is an input of the theorem below; it is proved elsewhere in the development.

**Theorem 7.3.5 (Hermitian symmetry of the transfer matrix).** Assume identities 1 to 6 and the star identity. Let $z, z' \in W_b$, let $\mu$ be a Haar measure on $G_i$, and let $f_1, f_2$ be smooth functions on $G_i$ with compact support. Then for all $Y \in \mathbb{C}$ and $p, q \in \{0, 1\}$,
$$\int_{G_i} T_{pq}(Y) f_1 \cdot \overline{f_2} \, d\mu = \int_{G_i} f_1 \cdot \overline{T_{qp}(\bar Y) f_2} \, d\mu.$$

Lean: `PI.QnHermHaar.qnHermHaar_of_alg` (also `PI.QnHermHaar.hermFromSteps_of_alg`, the same statement in curried form), `PI.QnHermHaar.glue_holds_var`.

*Proof.* Let $\mathcal{T}$ be the space of smooth compactly supported functions on $G_i$. We check that the operators of the problem form a $*$-algebra acting on $\mathcal{T}$. By identity 6 and the Leibniz rules, $\mathcal{E}_{ab}$, multiplication by $y_c$ and multiplication by $\bar y_c$ preserve $\mathcal{T}$, and the pairing $\int f_1 \bar f_2 \, d\mu$ is defined on $\mathcal{T}$. Identity 1 gives the adjoint of $\mathcal{E}_{ab}$ for this pairing: it is $\sum_{c,d} h_{cb} h_{ad} \mathcal{E}_{cd}$, where $h$ is the restriction of $H$ to the indices $i, \dots, i + m_i - 1$. This $h$ is Hermitian with $h^2 = 1$. The adjoint of multiplication by $y_l$ is multiplication by $\bar{y_l}$, and the definitions of $y$ and $\bar y$ give $\bar y_c = \sum_l h_{lc} \overline{y_l}$; the same holds for $x$ and $\bar x$. So the operators satisfy all the hypotheses of the star identity in the algebra of operators on $\mathcal{T}$ that have an adjoint. Each entry $T_{pq}(Y)$ is the image of $T^A_{pq}(u(Y))$, and $\overline{u(Y)} = u(\bar Y)$ since $(m_i - 1)/2$ is real. The star identity gives $T_{pq}(Y)^* = T_{qp}(\bar Y)$ as operators on $\mathcal{T}$, which is the claimed equality of integrals. $\square$

### Invariance under the stabilizers

**Theorem 7.3.6 (Invariance of the transfer matrix).** Assume identities 3 and 6 and that quantum minors of the $\mathcal{E}_{ab}$ commute with left translations. Let $z, z' \in W_b$ and let $D$ be an open set with $s g s' \in D$ for all $g \in G_i \cap D$, $s \in S_i(z)$ and $s' \in S_i(z')$. Let $f$ be smooth on $G_i \cap D$. Then for all $s \in S_i(z)$, $s' \in S_i(z')$, $g \in G_i \cap D$, $Y \in \mathbb{C}$ and $p, q$,
$$T_{pq}(Y)\big[x \mapsto f(s x s')\big](g) = \big(T_{pq}(Y) f\big)(s g s').$$

Lean: `Formalism.FourierDecayAlt.Q.TInvW.qnTInv_of`.

*Proof.* Right differentiation commutes with left translation, so each quantum minor commutes with $f \mapsto f(s \cdot)$. Left translation by $s \in S_i(z)$ leaves the functions $y$ and $\bar y$ unchanged, since $s$ fixes $f_i(z)$ and preserves the form. Right translation by $s'$ replaces the operators $\mathcal{E}$ by $P \mathcal{E} Q$, where $P$ and $Q = P^{-1}$ come from the adjoint action of $s'$, and it moves the vectors $x$ and $\bar x$ by the same matrices, because $s'$ fixes $f_i(z')$. Identity 3 says that the contractions that make up $T(Y)$ do not change. The steps use six proved lemmas: $1 \in S_i(z)$ and every $s \in S_i(z)$ lies in $G_i$ and fixes $f_i(z)$; $G_i$ is closed under products; $y(sg) = y(g)$ and $\bar y(sg) = \bar y(g)$ for $s \in S_i(z)$, while for $s' \in S_i(z')$ the block $B$ of $s'$ on the indices $i, \dots, i + m_i - 1$ is invertible, fixes $x$ and $\bar x$, and gives $y(g) = B\, y(g s')$ and $\bar y(g) = \bar y(g s') B^{-1}$; the value of $\mathcal{E}_{ab} f$ at $g$ depends only on $f$ on $G_i \cap D$; right translation gives $\mathcal{E}_{ab}[f(\cdot\, s')](g) = \sum_{c,d} (B^{-1})_{ca} B_{bd}\, (\mathcal{E}_{cd} f)(g s')$; and right translation by $s' \in G_i$ preserves smoothness on $G_i \cap D$. $\square$

**Remark 7.3.7 (Formalization).** The star identity is a hypothesis of the symmetry theorem; its caller supplies it. The name of the second declaration of the symmetry theorem is shared by five other theorems in other folders of the same part of the development, each proving a different statement. In the proof of the symmetry theorem the operators are realized in an abstract algebra of operators with adjoint on the test space, and the conclusion passes back to integrals through a representation lemma: see [RepresentsTransferOneOne.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/HermitianHaarMeasure/RepresentsTransferOneOne.lean#L117). The theorems are in [Assemble.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/HermitianHaarMeasure/Assemble.lean#L10) and [QnTInvOf.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/TorusInvariance/QnTInvOf.lean#L7).
