---
title: The big cell relation
decls:
  - GlobalTheory.KSp.weyl_cell_relation
  - GlobalTheory.T.exists_weilRepresentation_bigCell_relation_fourier
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The big cell relation

This section proves the one relation between the Siegel parabolic subgroup and the Weyl element that the Schrödinger model of the split unitary group needs: if $w p w$ lies in the big cell $PwP$, so that $wpw = p_1 w p_2$, then the operators of the model satisfy the same relation, with the Weyl element acting by a fixed multiple $\kappa$ of the Fourier transform. The constant $\kappa$ comes from [the Gauss integral](/entry/has-gauss-herm/) of the previous section. In [the next section](/entry/exists-is-kw/) this relation, together with the action of the Levi subgroup, extends the action of $P$ and $w$ to a representation of the whole group.

### The group and the operators

Keep the setting of [the previous section](/entry/has-gauss-herm/): $E/F$, $Q$, $\psi$, $\chi$, $\mu$ on $X = M_{m \times n}(E)$, the pairing $\langle x, y \rangle$ and the scalar $s(z) = \chi(z)|N_{E/F}(z)|_F^{m/2}$. Let
$$J = \begin{pmatrix} 0 & 1_n \\ -1_n & 0 \end{pmatrix}.$$

**Definition 1.3.1 (Split unitary group).** $G = \mathrm{U}(n,n)$ is the group of $g \in \mathrm{GL}_{2n}(E)$ with ${}^t g\, J\, \bar g = J$. The *Siegel parabolic* $P \subset G$ is the subgroup of $g \in G$ whose lower left $n \times n$ block is $0$. The *Weyl element* is $w = J$. The *big cell* is $PwP = \{p w q : p, q \in P\}$.

For $a \in \mathrm{GL}_n(E)$ and Hermitian $b \in M_n(E)$ put
$$m(a) = \begin{pmatrix} a & 0 \\ 0 & (a^*)^{-1} \end{pmatrix}, \qquad n(b) = \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix}.$$
Each element of $P$ is $m(a)\, n(b)$ for a unique pair $(a, b)$. This is the [parabolic subgroup](/learn/groups/#parabolic-subgroups) of Volume 1 that fixes the Lagrangian of the last $n$ coordinates.

Let $S = S(X)$ be the space of [[Schwartz-Bruhat functions|GE020MY43M]] on $X$: the locally constant functions with compact support.

**Definition 1.3.2 (Operators of the parabolic).** For $g \in P$ with upper blocks $A$ and $B$, and $\varphi \in S$, put
$$(\rho(g)\varphi)(x) = s(\det A)\, \psi\bigl(\tfrac12 \langle xA, xB \rangle\bigr)\, \varphi(xA).$$

**Definition 1.3.3 (Fourier transform).** For $\varphi \in S$ put $(\mathcal{F}\varphi)(x) = \int_X \psi(\langle x, y \rangle)\, \varphi(y)\, d\mu(y)$.

So $\rho(m(a))\varphi(x) = s(\det a)\varphi(xa)$ and $\rho(n(b))$ is multiplication by $\psi(\tfrac12\langle x, xb\rangle)$. These are the [Schrödinger model](/learn/theta/#the-schrdinger-model) formulas of Volume 1, with the splitting character $\chi$ in place of the quadratic character of an orthogonal space. Since $\psi \circ \langle\ ,\ \rangle$ is a self-dual pairing, $\mathcal{F}$ maps $S$ onto $S$, and $\mathcal{F}^2 \varphi(x) = C\varphi(-x)$ for a constant $C > 0$ that depends on $\mu$. Each $\rho(g)$ maps $S$ to $S$, and $\rho$ is a homomorphism on $P$.

### The relation

**Theorem 1.3.4 (Big cell relation).** There is $\kappa \in \mathbb{C}$ with $\kappa \neq 0$ such that for each $p \in P$ with $wpw \in PwP$ there are $p_1, p_2 \in P$ with $wpw = p_1 w p_2$ and
$$\kappa\mathcal{F}\,\rho(p)\,\kappa\mathcal{F}\,\varphi = \rho(p_1)\,\kappa\mathcal{F}\,\rho(p_2)\,\varphi$$
for all $\varphi \in S$.

Lean: `GlobalTheory.KSp.weyl_cell_relation` (also `GlobalTheory.T.exists_weilRepresentation_bigCell_relation_fourier`, a second name).

The main input is the Fourier transform of a Gaussian. Let $b$ be Hermitian and invertible, and write $\psi_b(x) = \psi(\tfrac12\langle x, xb\rangle)$. One has $\langle xb, y \rangle = \langle x, yb \rangle$, so completing the square gives
$$\tfrac12\langle y, yb \rangle + \langle x, y\rangle = \tfrac12\langle y', y'b\rangle - \tfrac12\langle x, xb^{-1}\rangle, \qquad y' = y + xb^{-1}.$$
By [the Gauss integral](/entry/has-gauss-herm/), the Fourier transform of $\psi_b$ is $\gamma_0\, s(\det b)^{-1}\, \psi_{-b^{-1}}$. This is why the composite $\mathcal{F}\rho(n(b))\mathcal{F}$ is again a product of operators of $P$ and $\mathcal{F}$.

**Lemma 1.3.5 (The Gauss constant is not zero).** The constant $\gamma_0$ of [the Gauss integral](/entry/has-gauss-herm/) is not $0$.

*Proof.* Let $L \subset X$ be a compact open subgroup and $\varphi$ its indicator function, so $\varphi \in S$ and $\varphi(0) = 1$. The identity for $\mathcal{F}\rho(n(1))\mathcal{F}\varphi$ obtained from the Gauss integral, with $b = 1$, has the factor $\gamma_0$ on one side, and on the other side the factor $s(\det(-1_n))$, which is not $0$, times $\mathcal{F}\rho(n(1))\mathcal{F}\varphi$. If $\gamma_0 = 0$, then $\mathcal{F}\rho(n(1))\mathcal{F}\varphi = 0$. The operator $\mathcal{F}$ is injective on $S$, since $\mathcal{F}^2$ is $C > 0$ times a reflection, and $\rho(n(1))$ is multiplication by a function with no zeros. So $\mathcal{F}\varphi = 0$, and then $\varphi = 0$, against $\varphi(0) = 1$. $\square$

*Proof of the theorem.* Put $\kappa = s(\det(-1_n))/\gamma_0$, which is defined and nonzero by the lemma. Let $p \in P$, and write $p = m(a)\, n(b)$. A block computation gives
$$wpw = \begin{pmatrix} -(a^*)^{-1} & 0 \\ ab & -a \end{pmatrix},$$
so the lower left block of $wpw$ is $ab$. An element of $G$ lies in $PwP$ if and only if its lower left block is invertible; so $wpw \in PwP$ means $\det b \neq 0$.

Now take $q = w\, m(a)\, w^{-1}$, which lies in $P$ (it is $m((a^*)^{-1})$), and
$$p_0 = \begin{pmatrix} -b^{-1} & 1 \\ 0 & -b \end{pmatrix} \in P.$$
A direct multiplication shows $w\, n(b)\, w = p_0\, w\, n(-b^{-1})$. Hence $wpw = q\, w\, n(b)\, w = (q p_0)\, w\, n(-b^{-1})$, and we take $p_1 = q p_0$ and $p_2 = n(-b^{-1})$.

For the operators, first take $a = 1$. The Fourier transform of a Gaussian, applied inside $\mathcal{F}\rho(n(b))\mathcal{F}$, gives
$$s(\det(-b^{-1}))\, \mathcal{F}\rho(n(b))\mathcal{F} = \gamma_0\, s(\det b)^{-1}\, \rho(p_0)\, \mathcal{F}\, \rho(n(-b^{-1}))$$
on $S$. Since $s$ is multiplicative, $\kappa\gamma_0\, s(\det b)^{-1} = s(\det(-1_n))\, s(\det b)^{-1} = s(\det(-b^{-1}))$, and multiplying by $\kappa^2 / s(\det(-b^{-1}))$ gives the relation for $p = n(b)$. For general $a$, the Levi factor passes through the Fourier transform: $\mathcal{F}\rho(m(a)) = \rho(q)\mathcal{F}$, by the substitution $y \mapsto ya$ in the integral and the adjoint property of the pairing. Since $\rho$ is a homomorphism on $P$, this gives
$$\kappa\mathcal{F}\rho(p)\kappa\mathcal{F} = \rho(q)\,\kappa\mathcal{F}\rho(n(b))\kappa\mathcal{F} = \rho(q p_0)\,\kappa\mathcal{F}\,\rho(n(-b^{-1})),$$
which is the claim. $\square$

**Remark 1.3.6.** The relation is the classical computation that the cocycle of the Weil representation is trivial on $\mathrm{U}(n,n)$ once the Levi acts through $\chi$; compare S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), Section 3. Here the constant of the Weyl element is fixed once, by the Gauss integral with $b = 1$.

**Remark 1.3.7 (Formalization).** The lemma that $\gamma_0 \neq 0$ is `GlobalTheory.KSp.WeylCellRel.gauss_const_ne_zero` (ExistsWeilRepresentationBigCellRelationFourier.lean, line 70), and the theorem is at line 130 of the same file. The operator identity for $n(b)$ is `fourier_hermitianMultiplier_braid_relation`, which takes the Gauss value for $b$ as a hypothesis; we have not opened its proof, so the completion of the square above is our account of it. The criterion for the big cell is `inCell_iff_det_lower_left_block_ne_zero` and the block formula is `lower_left`. The statement asks that the identity hold on $S$ only, and the second name is a `first | exact ...` wrapper (ExistsWeilRepresentationBigCellRelationFourierStatement.lean, line 9).
