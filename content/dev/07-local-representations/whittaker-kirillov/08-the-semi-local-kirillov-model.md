---
title: The semi-local Kirillov model
decls:
  - GlobalTheory.JSW.KirArchTransfer.kirillov_arch
  - GlobalTheory.JSW.MirPatch.exists_eq_on_mirS_of_slices
  - GlobalTheory.JSW.MirSemi.kirillov_semiLocal
  - GlobalTheory.JSW.MirSemi.kirillov_semilocal
  - GlobalTheory.JSW.KirSemi.kirillov_semilocal_bump
  - GlobalTheory.T.semiLocal_kirillov_archimedean_kernel_complexPlaces
  - GlobalTheory.T.exists_eq_on_mirabolic_of_slices_finitePlaces
  - GlobalTheory.T.kirillov_semiLocal_mirabolic_abstract
  - GlobalTheory.T.kirillov_semilocal_mirabolic_whittaker
  - GlobalTheory.T.kirillov_semilocal_smooth_bump
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The semi-local Kirillov model

This section moves the archimedean Kirillov theorem of the previous section ([Theorem 4.7.2](/entry/kirillov-cinf/)) to the adeles. Let $\pi$ be an irreducible space of cusp forms on $\mathrm{GL}_{m+1}$ over a totally complex field, and let $S$ be a finite set of finite places. If the global Whittaker coefficient of one form of $\pi$ is nonzero at one point of the semi-local group of $S$, then every smooth Whittaker function on the semi-local mirabolic group that is compactly supported modulo $N$ is the Whittaker coefficient of a form in the closure of $\pi$ under translations and rapid kernels. The form can be chosen with the same invariance as the given one outside $S$. The final result is used in the proof of [Theorem 8.7.6 of Volume 8](/entry/vanish/). For Whittaker coefficients of cusp forms, see [Fourier coefficients and Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions).

We prove four results, from the archimedean slice to the bump form: a transfer of the archimedean theorem to one slice, a patching lemma over the finite places, an abstract semi-local theorem, and two forms for cusp forms.

### Notation

Let $E$ be a totally complex number field with adele ring $\mathbb{A} = E_\infty \times \mathbb{A}_f$, $n = m + 1$ and $G = \mathrm{GL}_n(\mathbb{A})$. Let $N \subset G$ be the upper unitriangular group, $\psi$ the standard additive character of $\mathbb{A}/E$ and $\psi_N(u) = \psi(\sum_i u_{i,i+1})$. We write $\iota \colon \mathrm{GL}_n(E_\infty) \to G$ for the inclusion at the archimedean places. On $\iota(N_\infty)$ the character $\psi_N$ is the character $\psi_\infty$ of the previous section, $\psi_N(\iota(u)) = e(-\sum_w 2\operatorname{Re}\sum_i u_{i,i+1,w})$.

**Definition 4.8.1 (Semi-local groups).** The *semi-local group* $G_S$ is the set of $g \in G$ with $g_w = 1$ at each finite place $w \notin S$. The *semi-local mirabolic set* $P_S$ is the set of $g \in G_S$ whose last row is $(0, \ldots, 0, 1)$.

So $G_S = \mathrm{GL}_n(E_\infty) \times \prod_{w \in S}\mathrm{GL}_n(E_w)$. A *slice* of $P_S$ is the set of $q\,\iota(y) \in P_S$ for a fixed $q$ with $q_\infty = 1$. Since $q$ and $\iota(y)$ commute and have disjoint support, $q\,\iota(y) \in P_S$ holds exactly when $q \in P_S$ and $y \in P_\infty$, or the slice is empty.

Let $\phi$ be a function on $G$. Its *Whittaker coefficient* is
$$W_\phi(g) = \int_{N(E)\backslash N(\mathbb{A})} \phi(ug)\, \overline{\psi_N(u)}\, du.$$
A *rapid kernel* is as in the previous section; its operator on functions on $G$ is
$$F \mapsto \Big(g \mapsto \int_X k(x)\, F(g\,\iota(\gamma(x)))\, d\nu(x)\Big).$$

**Definition 4.8.2 (Admissible target).** A function $b$ on $G$ is an *admissible target* if:

1. $b(ug) = \psi_N(u) b(g)$ for $u \in N(\mathbb{A})$;
2. there is a compact $C \subset G$ such that each $p \in P_S$ with $b(p) \neq 0$ lies in $N(\mathbb{A})C$;
3. $b$ is right invariant under an open subgroup $U \subset \mathrm{GL}_n(\mathbb{A}_f)$;
4. for each $g$, the function $x \mapsto b(g\,\iota(x))$ on invertible matrices over $E_\infty$ (extended by $0$) is smooth on invertible matrices.

These are the conditions of a Kirillov function on $P_S$: Whittaker equivariance, compact support modulo $N$, smoothness at the finite places of $S$ and at the infinite places.

### The archimedean slice

**Theorem 4.8.3 (Transfer to a slice).** Let $q \in G$ with $q_\infty = 1$. Let $W$ be a function on $G$ with $W(ug) = \psi_N(u)W(g)$, with $y \mapsto W(q\,\iota(y))$ continuous and bounded by $C'\|y\|^N$, and with $W(q) \neq 0$. Let $b$ satisfy conditions 1 and 2, with $x \mapsto b(q\,\iota(x))$ smooth on invertible matrices. Then there is a rapid kernel with
$$\int_X k(x)\, W(q\,\iota(y)\,\iota(\gamma(x)))\, d\nu(x) = b(q\,\iota(y))$$
for every $y$ with $q\,\iota(y) \in P_S$.

Lean: `GlobalTheory.JSW.KirArchTransfer.kirillov_arch` (also `GlobalTheory.T.semiLocal_kirillov_archimedean_kernel_complexPlaces`, a second name).

*Proof.* If $q \notin P_S$ the slice is empty, and the Dirac kernel at one point satisfies the empty condition. Let $q \in P_S$. Then $q\,\iota(y) \in P_S$ if and only if $y \in P_\infty$. Put $\beta(y) = b(q\,\iota(y))$ and $f(y) = W(q\,\iota(y))$. Since $q$ commutes with $\iota(u)$, both are $\psi_\infty$-equivariant under $N_\infty$. The function $f$ is continuous with moderate growth and $f(1) = W(q) \neq 0$. The compact set $C$ of condition 2 projects to a compact subset of $\mathrm{GL}_n(E_\infty)$, and it controls the support of $\beta$ on $P_\infty$ modulo $N_\infty$. Apply [Theorem 4.7.2](/entry/kirillov-cinf/). $\square$

### Patching over the finite places

**Lemma 4.8.4 (Patching).** Let $\mathcal{W}$ be a space of functions on $G$, each of which is $\psi_N$-equivariant, right invariant under some open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$, and such that $\mathcal{W}$ is stable under right translation by $G_S$. Let $b$ satisfy conditions 1 to 3. Assume that for each $q$ with $q_\infty = 1$ there is $W_q \in \mathcal{W}$ with $W_q = b$ on the slice of $q$. Then there is $W \in \mathcal{W}$ with $W = b$ on $P_S$.

Lean: `GlobalTheory.JSW.MirPatch.exists_eq_on_mirS_of_slices` (also `GlobalTheory.T.exists_eq_on_mirabolic_of_slices_finitePlaces`, a second name).

*Proof.* Let $K \subset \prod_{w \in S}\mathrm{GL}_n(\mathcal{O}_w)$ be an open compact subgroup that fixes $b$ on the right.

1. The support of $b$ on $P_S$ lies in $N(\mathbb{A})C$ with $C$ compact. So it is covered by finitely many disjoint cells $N(\mathbb{A})\, x_i K\, \mathrm{GL}_n(E_\infty)$ with $x_i$ supported at $S$.
2. For each cell there are finitely many $h_j \in G_S$ supported at $S$ and numbers $c_j$ such that $\sum_j c_j W(p h_j) = \mathbf{1}_{\text{cell}}(p) W(p)$ for $p \in P_S$ and $W$ in $\mathcal{W}$ invariant under a small enough subgroup. This is the usual cut-off by averages over compact open subgroups at the places of $S$.
3. On one cell, $W_{x_i}$ agrees with $b$ on the slice of $x_i$. By the $\psi_N$-equivariance of both and their right invariance under $K$ (after shrinking $K$), they agree on the whole cell.
4. Apply the cut operator of each cell to $W_{x_i}$ and add over $i$. The sum is in $\mathcal{W}$ by stability under $G_S$, and it equals $b$ on $P_S$.

$\square$

### The abstract semi-local theorem

**Theorem 4.8.5 (Abstract semi-local Kirillov theorem).** Let $\mathcal{W}$ be a space of functions on $G$ with these properties:

1. each $W \in \mathcal{W}$ satisfies $W(ug) = \psi_N(u)W(g)$;
2. $\mathcal{W}$ is stable under right translation by $G_S$;
3. $\mathcal{W}$ is stable under the operators of rapid kernels;
4. for each $W \in \mathcal{W}$ and $g$, the function $y \mapsto W(g\,\iota(y))$ is continuous and bounded by $C'\|y\|^N$;
5. each $W \in \mathcal{W}$ is right invariant under an open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$.

Assume that some $W_0 \in \mathcal{W}$ has $W_0(p_0) \neq 0$ for one $p_0 \in P_S$. Then for each admissible target $b$ there is $W \in \mathcal{W}$ with $W = b$ on $P_S$.

Lean: `GlobalTheory.JSW.MirSemi.kirillov_semiLocal` (also `GlobalTheory.T.kirillov_semiLocal_mirabolic_abstract`, a second name).

*Proof.* By the patching lemma it is enough to treat one slice, of $q$ with $q_\infty = 1$ and $q \in P_S$. The element $q^{-1}p_0$ is in $G_S$, so $W'(g) = W_0(g\,q^{-1}p_0)$ is in $\mathcal{W}$ by property 2, and $W'(q) = W_0(p_0) \neq 0$. By properties 1 and 4 and conditions 1, 2 and 4 of the target, the transfer theorem applies to $W'$ and $b$ at $q$. It gives a rapid kernel whose operator sends $W'$ to a function equal to $b$ on the slice. This function is in $\mathcal{W}$ by property 3. $\square$

### Cusp forms

Let $\mathcal{A}_0$ be the space of cusp forms on $\mathrm{GL}_n(E)\backslash G$ that are smooth in the archimedean variable: for each $g$, $x \mapsto \phi(g\,\iota(x))$ is smooth on invertible matrices. Let $\pi \subset \mathcal{A}_0$ be an irreducible subspace stable under $G$. Let $\overline{\pi}$ be the smallest space of functions on $G$ that contains $\pi$ and is stable under right translation by $G$ and under the operators of rapid kernels.

**Theorem 4.8.6 (Semi-local Kirillov model, mirabolic form).** Let $\phi \in \pi$ with $W_\phi(p) \neq 0$ for some $p \in P_S$. Let $b$ be an admissible target. Then there is $F \in \overline{\pi}$ such that:

1. $W_F = b$ on $P_S$;
2. $F$ is right invariant under an open subgroup of $\mathrm{GL}_n(\mathbb{A}_f)$;
3. for each $t \in G$ with $t_\infty = 1$ and $t_w = 1$ for $w \in S$: if $\phi$ is right invariant under $t$, then so is $F$;
4. if $c \in \mathbb{C}$ and $t$ satisfy $W_\phi(xt) = cW_\phi(x)$ for all $x \in G_S$, then $W_F(xt) = cW_F(x)$ for all $x \in G_S$.

Lean: `GlobalTheory.JSW.MirSemi.kirillov_semilocal` (also `GlobalTheory.T.kirillov_semilocal_mirabolic_whittaker`, a second name).

*Proof.* Let $\Sigma$ be the space of forms obtained from $\phi$ by finitely many right translations by $G_S$ and rapid kernels, and let $\mathcal{W}$ be the space of their Whittaker coefficients. The Whittaker coefficient commutes with right translations and, by Fubini, with the operators of rapid kernels. So $\mathcal{W}$ has properties 2 and 3 of the abstract theorem. Property 1 holds by the definition of $W_\phi$. Property 4 follows from the moderate growth of cusp forms, and property 5 from the smoothness of $\phi$ at the finite places, preserved by translations and archimedean kernels. The abstract theorem gives $F \in \Sigma$ with $W_F = b$ on $P_S$. Since $\Sigma \subset \overline{\pi}$, this proves 1. Properties 2 to 4 hold for $\phi$ and are preserved by right translation by $G_S$ and by archimedean kernels, because such $t$ commute with $G_S$. $\square$

**Theorem 4.8.7 (Semi-local Kirillov model).** Let $\phi \in \pi$ with $W_\phi(x) \neq 0$ for some $x \in G_S$. Let $b$ be an admissible target. Then there is $F \in \overline{\pi}$ with properties 1 to 4 of the mirabolic form.

Lean: `GlobalTheory.JSW.KirSemi.kirillov_semilocal_bump` (also `GlobalTheory.T.kirillov_semilocal_smooth_bump`, a second name).

*Proof.* We move $x$ into $P_S$.

1. By the Iwasawa decomposition at the archimedean places, $x_\infty = p_0\,\rho\,k$ with $p_0$ in the archimedean mirabolic group, $\rho$ a scalar and $k$ compact.
2. The value $W_\phi(x)$ is continuous in the scalar $\rho$, and $E^\times$ is dense in $E_\infty^\times$. So there is $\beta \in E^\times$ with $W_\phi(p_0\,\beta_\infty\,k\,x_f) \neq 0$.
3. Put $s = \beta_\infty\,k\,x_f$. It lies in $G_S$. The form $\psi(g) = \phi(gs)$ is in $\pi$. Since $\phi$ is left invariant under the rational scalar $\beta$, the Whittaker coefficient of $\psi$ is $W_\psi(g) = W_\phi(gs)$, and $W_\psi(p_0) \neq 0$ with $p_0 \in P_S$.
4. Each $t$ in properties 3 and 4 is $1$ at the places of $S$ and at infinity, so it commutes with $s$. So $\psi$ inherits these properties from $\phi$.
5. Apply the mirabolic form to $\psi$.

$\square$

**Remark 4.8.8 (Formalization).** The two theorems `MirSemi.kirillov_semilocal` and `MirSemi.kirillov_semiLocal` differ only in one capital letter ([KirillovSemilocalMirabolicWhittaker.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemilocalMirabolicWhittaker.lean#L16), [KirillovSemiLocalMirabolicAbstract.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/KirillovSemiLocalMirabolicAbstract.lean#L16)), but one is about cusp forms and the other is about an abstract space. The transfer theorem is vacuous on an empty slice, where it uses a Dirac kernel ([SemiLocalKirillovArchimedeanKernelComplexPlaces.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiLocalKirillovArchimedeanKernelComplexPlaces.lean)). Smoothness is written both with `ContDiffOn ℝ ∞` and with the order `((⊤ : ℕ∞) : WithTop ℕ∞)`; they agree. The cut operators of step 2 of the patching lemma and the Iwasawa step of the bump form are summarized, not stated.
