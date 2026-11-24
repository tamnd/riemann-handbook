---
title: Fibre volumes of normal-form stabilizers
decls:
  - GlobalTheory.Amp.FibreNormal.fibre_volume
  - GlobalTheory.T.flagUnipotent_gramNull_and_fibreVolume_normalForm
  - GlobalTheory.Amp.FibreVolume.fibre_volume
  - GlobalTheory.T.fibreVolume_normalFormStabiliser
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Fibre volumes of normal-form stabilizers

This section and the next one work at one real place of the CM field. There the unitary group is a real Lie group $U(r+k, r+1)$, and the amplitude of a degenerate term is an integral over a unipotent group. We bound the volume of the set of unipotent elements that put a given element into a fixed box and that give a Gram volume in a fixed dyadic range. The bound is first proved for elements in normal form and then for any element with a normal-form stabilizer measure. The next section uses it to bound the side pieces of the degenerate amplitude, and from there it enters the [amplitude bound at terms](/entry/amplitude-bound-of-local-data-of-tail-bound/).

**Definition 2.6.1 (The archimedean setting).** Let $k, r \ge 0$ be integers and put $n = 2r + k + 1$. Index the standard basis of $\mathbb{C}^n$ by $0, \dots, n - 1$. For $a < r$ write $e_a$ for the basis vector with index $a$ and $e_a^*$ for the basis vector with index $2r + k - a$. The indices $r, \dots, r + k$ form the middle block. Let $H$ be the Hermitian matrix with $H e_a = e_a^*$ and $H e_a^* = e_a$ for $a < r$, and which is the identity on the middle block except for the entry $-1$ at index $r + k$. Write $h(v, w)$ for the [[Hermitian form|8NJ7XY6F1S]] with matrix $H$ and $G = U(H)$ for its unitary group. The spaces $X = \langle e_0, \dots, e_{r-1}\rangle$ and $X^* = \langle e_0^*, \dots, e_{r-1}^*\rangle$ are totally isotropic, and the middle block $W_b \cong \mathbb{C}^{k+1}$ carries the form $H_b = \mathrm{diag}(1, \dots, 1, -1)$. For $z \in W_b$ put $T(z) = -\operatorname{Re} h(z, z)$, so $T(z) > 0$ means that $z$ is a negative vector.

The group $G$ is the real points of the unitary group of the section on [unitary groups](/learn/groups/#unitary-groups). The flag $X_1 \subset \dots \subset X_r = X$ with $X_a = \langle e_0, \dots, e_{a-1}\rangle$ is a full isotropic flag, and we use the unipotent radical of its stabilizer.

**Definition 2.6.2 (The flag unipotent group).** Let $N$ be the set of $g \in G$ with $g e_a \in e_a + X_a$ for every $a < r$ and $g w \in w + X$ for every $w \in W_b$. It is the unipotent radical of the [parabolic subgroup](/learn/groups/#parabolic-subgroups) that fixes the flag $(X_a)$ and acts trivially on $X^\perp / X$. The group $N$ has explicit coordinates: an upper unitriangular $r \times r$ matrix and a point of a parameter space for the part that moves $W_b$ and $X^*$. Let $dn$ be the image of Lebesgue measure on these coordinates. It is a Haar measure on $N$, and $N$ is unimodular.

For two vectors $z, z' \in W_b$ we use the flags $f_a = e_a$ for $a < r$, $f_r = z$, and $f'_a = e_a$ for $a < r$, $f'_r = z'$.

**Definition 2.6.3 (Gram minors, sizes and Gram volume).** Let $\gamma, x \in G$.

1. The [[Gram matrix|00SPJSDT3Z]] of $\gamma$ is the $(r+1) \times (r+1)$ matrix $\hat Z(\gamma)_{ab} = h(\gamma f'_b, f_a)$. For $0 \le l \le r + 1$ let $D_l(\gamma)$ be the determinant of its leading $l \times l$ minor.
2. For $a \le r$ let $\lambda_a(z, x)$ be the infimum of the Euclidean norms $\|x^{-1}(f_a - y)\|$ over $y \in X_a$. The size of $x$ is
$$S_z(x) = \max\Bigl(1, \max_{a \le r} \max(\lambda_a(z,x), \lambda_a(z,x)^{-1})\Bigr).$$
3. Let $H_{\mathrm{com}}(\gamma)$ be the space of $w$ with $h(w, f'_a) = 0$ and $h(w, \gamma^{-1} f_a) = 0$ for all $a \le r$. Let $P_+(\gamma, x)$ be the intersection of the $+1$ eigenspace of the matrix $H$ with $x^{-1}(H_{\mathrm{com}}(\gamma) + X)$. For a subspace $P$ and vectors $v_1, \dots, v_j$, let $\mathrm{vol}_P(v_1, \dots, v_j)$ be the square root of the absolute value of the Gram determinant of the orthogonal projections $\pi_P v_1, \dots, \pi_P v_j$.
4. For $1 \le j \le r$ the normalized Gram volume is
$$Y_j(\gamma, x) = \frac{\mathrm{vol}_{P_+(\gamma,x)}\bigl(x^{-1}\gamma^{-1} e_0, \dots, x^{-1}\gamma^{-1} e_{j-1}\bigr)}{|D_j(\gamma)|}.$$

The size $S_z(x)$ measures how far $x$ is from the maximal compact subgroup in the directions of the flag. The number $Y_j$ is the quantity whose small values make a term degenerate.

**Definition 2.6.4 (Minor bound).** A real number $D_e$ is a minor bound for $\gamma$ if $D_e \ge 1$ and $|D_l(\gamma)|^{-1} \le D_e$ for every $l \le r$ with $D_l(\gamma) \ne 0$.

**Definition 2.6.5 (Normal element).** Let $0 \le j \le r$, let $\beta : \{0, \dots, r-1\} \to \mathbb{N}$ and let $c \in \mathbb{C}$. An element $g_0$ is normal with data $(j, \beta, c)$ for $(z, z')$ if: $g_0 \in G$; $|c| = 1$; $g_0 z' = c z$; $\beta$ is monotone; for $b \ge j$ one has $\beta(a) = \beta(b)$ exactly when $a \ge j$; for $a < j$ both $g_0 e_a$ and $g_0^{-1} e_a$ lie in $\langle e_b^* : b < j\rangle$; for $a \ge j$ one has $g_0 e_a = c e_a$ and $g_0 e_a^* = c e_a^*$; and the $j \times j$ corner of a matrix attached to $g_0$ is block antidiagonal for the blocks on which $\beta$ is constant.

So a normal element swaps the first $j$ isotropic lines with their duals, acts by the scalar $c$ on the remaining hyperbolic planes, and carries $z'$ to a multiple of $z$.

**Definition 2.6.6 (Normal-form stabilizer measure).** For data $(j, \beta)$ let $\mu^0_\beta$ be the image of Lebesgue measure under an explicit polynomial parametrization of the common stabilizer of a normal element with these data. Let $\gamma \in G$ and $s > 0$. A measure $\mu_R$ is a normal-form stabilizer measure for $\gamma$ with scale $s$ if $z, z' \in W_b$, $T(z) > 0$, and there are $n_1, n_2 \in N$ and a normal element $g_0$ with data $(j, \beta, c)$ such that $\gamma = n_1 g_0 n_2$ and $\mu_R$ is the image of $s\,\mu^0_\beta$ under conjugation by $n_2^{-1}$.

**Definition 2.6.7 (Cutoff and fibre set).** Let $S$ be a set of matrices and $\mu$ a measure on matrices. A cutoff for $(S, \mu)$ is a measurable $\varphi \ge 0$ (with values in $[0, \infty]$) with
$$\int \varphi(\rho x)\, d\mu(\rho) \le 1 \quad \text{for every } x \in S.$$
For $R_0, y > 0$ the fibre set $E(\gamma; R_0, y)$ is the set of $x \in G$ with
$$S_{z'}(x) \le R_0, \quad S_z(\gamma x) \le R_0, \quad y < Y_j(\gamma, x) \le 2y.$$
The fibre volume is
$$\begin{aligned} V(R_0, D_e, y) = {} & (4r)^{4r^2} (R_0^{2r} D_e)^{8r^2} \\ & \cdot \Bigl(\frac{\pi e}{k-1-j}\Bigr)^{j(k-1-j)} (2y)^{2(k-1-j)}. \end{aligned}$$

The cutoff is a function that integrates to at most $1$ over each orbit of the stabilizer. It lets us count a stabilizer orbit once.

For $a \in \mathbb{R}_{>0}^r$ and $m \in U(H_b)$ let $t(a, m)$ be the element of $G$ that acts by $\mathrm{diag}(a)$ on $X$, by the inverse adjoint on $X^*$, and by $m$ on $W_b$. These are the elements of the Levi part in the Iwasawa decomposition.

**Theorem 2.6.8 (Fibre volume in normal form).** Let $z, z' \in W_b$ with $T(z) > 0$. Let $1 \le j$ with $j + 2 \le k$ and $j \le r$. Let $g_0$ be normal with data $(j, \beta, c)$ for $(z, z')$, let $D_e$ be a minor bound for $g_0$, let $m \in U(H_b)$ and $a \in \mathbb{R}_{>0}^r$, and put $t = t(a, m)$. Then:

1. the set of $n$ with $Y_j(g_0, n t) = 0$ has $dn$-measure $0$;
2. for every cutoff $\varphi$ for $(N, \mu^0_\beta)$ and all $R_0 \ge 1$, $y > 0$,
$$\int_N \varphi(n)\, \mathbf{1}_{E(g_0; R_0, y)}(n t)\, dn \le V(R_0, D_e, y).$$

Lean: `GlobalTheory.Amp.FibreNormal.fibre_volume` (also `GlobalTheory.T.flagUnipotent_gramNull_and_fibreVolume_normalForm`, a second name).

*Proof.* First, $T(z') = T(z)$, because $g_0$ is unitary, $g_0 z' = c z$ and $|c| = 1$. So both flags consist of a negative vector over an isotropic flag. The common stabilizer $R(g_0)$ of the two flags under $g_0$ is a closed set, and it equals the image of the parametrization that defines $\mu^0_\beta$. So $\mu^0_\beta$ is carried by $R(g_0)$.

Next we split $N$. There is a section $q \mapsto s(q)$ with coordinates $q = (q_1, q_2)$ such that for each measurable $F \ge 0$
$$\int_N F(n)\, dn = \int \int F(\rho\, s(q))\, d\mu^0_\beta(\rho)\, dq.$$
The first coordinate block $q_1$ contains $j$ vectors $B_0(q), \dots, B_{j-1}(q) \in \mathbb{C}^{k+1}$. The normalized Gram volume is invariant under left multiplication by elements of $R(g_0)$, and in normal form it is a Gram volume in $\mathbb{C}^{k+1}$: there is a subspace $P_0 \subseteq \mathbb{C}^{k+1}$ of dimension at least $k - 1$ such that for $\rho \in R(g_0)$
$$Y_j(g_0, \rho\, s(q)\, t) = \mathrm{vol}_{P_0}\bigl(m^{-1} B_0(q), \dots, m^{-1} B_{j-1}(q)\bigr).$$

We use a volume estimate in $\mathbb{C}^{k+1}$. For $m \in U(H_b)$ and $P_0$ of dimension at least $k - 1$, with $1 \le j$ and $j + 2 \le k$: the set of $j$-tuples $B$ with $\mathrm{vol}_{P_0}(m^{-1} B) = 0$ is Lebesgue null, and for $M \ge 1$ and $y > 0$ the set of $B$ with $\|m^{-1} B_b\| \le M$ for all $b$ and $\mathrm{vol}_{P_0}(m^{-1} B) \le 2y$ has volume at most
$$2 (\pi M^2)^{2j} M^{2j^2} \pi^{j^2} \Bigl(\frac{\pi e}{k-1-j}\Bigr)^{j(k-1-j)} (2y)^{2(k-1-j)}.$$

Part 1 follows. By the splitting, the measure of the zero set is an integral over $q$ of the $\mu^0_\beta$-measure of a set that is empty unless $B(q)$ lies in the null set above. So the integrand vanishes for almost every $q$.

For part 2, the cutoff property on $N$ bounds the inner integral over $\rho$ by $1$ whenever $s(q) t$ lies in the fibre set. A height bound on the section says: if $S_{z'}(s(q) t) \le R_0$ and $S_z(g_0 s(q) t) \le R_0$, then with $M = R_0^{2r} D_e$ every coordinate of $q_2$ and every vector $m^{-1} B_b(q)$ has norm at most $M$, and the remaining coordinates of $q_1$ have absolute value at most $2 r M^2$. So the outer integral is at most the volume of a product of discs, intervals and the Gram set above. The Gram set gives the last two factors of $V$. The discs, the intervals and the remaining factors of the Gram estimate are powers of $\pi$, of $2rM^2$ and of $M$, and an elementary estimate with $j \le r$ and $M \ge 1$ bounds their product by $(4r)^{4r^2} M^{8r^2}$. This is the bound $V(R_0, D_e, y)$. $\square$

**Theorem 2.6.9 (Fibre volume for a normal-form stabilizer measure).** Let $1 \le j$ with $j + 2 \le k$ and $j \le r$. Let $\gamma \in G$, let $D_e$ be a minor bound for $\gamma$, let $s > 0$, and let $\mu_R$ be a normal-form stabilizer measure for $\gamma$ with scale $s$. Let $g_1 \in G$. Then:

1. the set of $n$ with $Y_j(\gamma, n g_1) = 0$ has $dn$-measure $0$;
2. for every cutoff $\varphi$ for $(G, \mu_R)$ and all $R_0 \ge 1$, $y > 0$,
$$\int_N \varphi(n g_1)\, \mathbf{1}_{E(\gamma; R_0, y)}(n g_1)\, dn \le \frac{V(R_0, D_e, y)}{s}.$$

Lean: `GlobalTheory.Amp.FibreVolume.fibre_volume` (also `GlobalTheory.T.fibreVolume_normalFormStabiliser`, a second name).

*Proof.* Write $\gamma = n_1 g_0 n_2$ with $g_0$ normal with data $(j, \beta, c)$, as in the definition of $\mu_R$. By the Iwasawa decomposition for the isotropic flag, $g_1 = n_0\, t\, \kappa$ with $n_0 \in N$, $t = t(a, m)$ for some $a \in \mathbb{R}_{>0}^r$ and $m \in U(H_b)$, and $\kappa$ in the maximal compact subgroup.

The minors $D_l$ do not change when $\gamma$ is multiplied on the left and on the right by elements of $N$, because $N$ preserves the flags $(f_a)$ and $(f'_a)$ up to lower terms. So $D_e$ is a minor bound for $g_0$, and the [Theorem 2.6.8](/entry/fibre-normal-fibre-volume/) applies to $g_0$ and $t$.

Change variables by $n \mapsto n_2 n n_0$ on $N$. This map preserves $dn$, since $N$ is unimodular. The normalized Gram volume has two invariances: $Y_j(n_1 g_0 n_2, x) = Y_j(g_0, n_2 x)$ for $n_1, n_2 \in N$, and $Y_j(g_0, x \kappa) = Y_j(g_0, x)$ for $\kappa$ in the maximal compact subgroup. The size $S_z$ has the same invariances: it does not change under left multiplication by $N$ and right multiplication by the maximal compact subgroup. So for $n \in N$
$$Y_j(\gamma, n g_1) = Y_j(g_0, n_2 n n_0 t),$$
and $n g_1 \in E(\gamma; R_0, y)$ exactly when $n_2 n n_0 t \in E(g_0; R_0, y)$.

Part 1 now follows from part 1 of the normal case. For part 2 put $\psi(x) = s\, \varphi(n_2^{-1} x\, n_0^{-1} g_1)$, with $n_0^{-1} g_1 = t \kappa$. Then $\psi(n_2 n n_0) = s\, \varphi(n g_1)$. Since $\mu_R$ is the image of $s\,\mu^0_\beta$ under conjugation by $n_2^{-1}$, the cutoff property of $\varphi$ for $(G, \mu_R)$ at the point $n_2^{-1} x\, t\kappa$ gives the cutoff property of $\psi$ for $(N, \mu^0_\beta)$. So
$$s \int_N \varphi(n g_1)\, \mathbf{1}_{E(\gamma)}(n g_1)\, dn = \int_N \psi(n)\, \mathbf{1}_{E(g_0)}(n t)\, dn \le V(R_0, D_e, y),$$
by part 2 of the normal case. Divide by $s$. $\square$

**Remark 2.6.10.** The bound has the factor $(2y)^{2(k-1-j)}$. For small $y$ the set of unipotent elements with a small Gram volume is small, and the exponent grows with the codimension $k - 1 - j$. This is why the next section asks for $j + 2 \le k$.

**Remark 2.6.11 (Formalization).** The measure $\mu^0_\beta$ is `lebR0`, the image of Lebesgue measure under the parametrization `rEl`; we have not unfolded `rEl` or the matrix and block condition in the last clause of `IsNormal0` (`Zr`, `BlockAnti`), so the text describes them only in words. In the normal case the cutoff condition is asked on $N$ only, while in the general case it is asked on all of $G$ ([FibreVolumeNormalFormStabiliser.lean](lean:Development/AbelianVarietyTheory/Proofs/FlagMeasures/FibreVolumeNormalFormStabiliser.lean#L79)). The integrals are over all matrices with respect to `lebN`, which is carried by $N$. The steps of the proofs (the splitting of `lebN`, the Gram volume bound `vol_gram`, the height bound `siegel_height_bound_section`, the Iwasawa decomposition) are separate results of other chapters or of later parts of this chapter. The second names are wrappers of the form `first | exact @X | exact X | ...`.
