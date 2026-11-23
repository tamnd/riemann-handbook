---
title: Local orbit volumes at the finite places
decls:
  - PI.OmVg.omVBadT_of_ffX
  - Formalism.L2.SG.Pf.NcVal.OmVSt.OmVZ.omVBadT_holdsX
  - Formalism.L2.SG.Pf.NcX.OmVSt.omVZ_holdsX
  - Formalism.L2.SG.Pf.NcVal.OmVSt.OmVZ.omV_holdsX
  - Formalism.L2.SG.Pf.NcVal.volTypV_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local orbit volumes at the finite places

At a finite place $v$ of $F$ the analogue of the orbit constant is a volume: the measure, in the fibre over its Gram matrix, of the orbit of a frame under the stabilizer $K_v$ of a lattice. This section computes it. Away from the divisors of $T_{u'}$ the frame is unimodular and the answer is the classical local density of a unimodular lattice. At a divisor of $T_{u'}$ the Gram matrix has corank one modulo $v$, and the product gains one factor. We also compute the ratio of two congruence volumes at the typed places. The results feed the [local tie of orbit volumes](/entry/nc-tie0-all-of/) and the [nonemptiness of the hypotheses](/step/nonempty-hyps/).

### Self-dual measures and the fibre volume

Let $E / F$ be a CM extension with Galois involution $x \mapsto \bar x$, and let $V = E^n$ with a nondegenerate [Hermitian form](/learn/algebra/#hermitian-and-skew-hermitian-forms) $h$. Let $\Lambda \subseteq V$ be an $\mathcal{O}_E$-lattice. Let $v$ be a finite place of $F$ with completion $F_v$, residue field of order $q_v = N(v)$, and $E_v = F_v \otimes_F E$; let $\Lambda_v$ be the closure of $\Lambda$ in $V_v = E_v^n$, and let $K_v$ be the stabilizer of $\Lambda_v$ in $\mathrm{U}(V_v)$. Let $\mathfrak{d}_v \in F_v$ be a generator of the local different, so $|\mathfrak{d}_v|_v$ is the $v$-part of the different of $F$. Let $\eta_v = 1$ if $v$ splits in $E$ (that is, $E_v$ has a nontrivial idempotent) and $\eta_v = -1$ otherwise.

Let $\psi$ be a [standard additive character](/learn/class-field-theory/#additive-characters) of $\mathbb{A}_F / F$ and $\psi_v$ its component at $v$. On the space of $a$-tuples of vectors of $V_v$ and on the space of Hermitian matrices of size $a$ over $E_v$ we take the measures that are self-dual for $\psi_v$ and the trace pairings. As at infinity, a *fibre family* is a family of measures $\omega_T$ on tuples, indexed by Hermitian matrices $T$, such that $\omega_T$ lives on the linearly independent tuples with Gram matrix $T$ and the self-dual measure on tuples is $\int \omega_T \, dT$.

**Definition 5.5.1 (Local orbit volume).** For a Hermitian matrix $T$ of size $a$ over $E_v$, let $\omega_T$ be the fibre measure at $T$ of the fibre family. For an $a$-tuple $Y$ with Gram matrix $T$, the *local orbit volume* of $Y$ is $\omega_T(K_v Y)$, the measure of the orbit of $Y$ under $K_v$ in the fibre over $T$.

Lean: `Formalism.L2.SG.LocVol.omAt`.

When the fibre family is unique, the local orbit volume is the local density of representations of $T$ by $\Lambda_v$, restricted to the primitive representations in one orbit. See the [local densities](/learn/hermitian-lattices/#local-densities) of Volume 1.

A tuple $Y = (y_1, \dots, y_a)$ is *primitive* in $\Lambda_v$ if every $y_i$ lies in $\Lambda_v$, and $\sum_i c_i y_i \in \Lambda_v$ with $c_i \in E_v$ implies $c_i \in \mathcal{O}_{E_v}$ for all $i$. The lattice $\Lambda$ is *self-dual at* $v$ if $\Lambda_v$ is its own dual for $h$.

The basic case is the unimodular one. Let $\Lambda$ be self-dual at $v$, let $v$ be unramified in $E$, and let $Y$ be a primitive $a$-tuple, $a \leq n$, whose Gram matrix has a unit determinant. Then
$$\omega_T(K_v Y) = |\mathfrak{d}_v|_v^{\,n a - a^2 / 2} \prod_{j = n - a + 1}^{n} \big(1 - \eta_v^j q_v^{-j}\big).$$
We take this unimodular formula as proved; it is the primitive local density of a unimodular Hermitian lattice, in the normalization of the self-dual measures (compare Gan, Hanke and Yu, cited at the end of the chapter).

### The frame of a word

Fix $r \geq 0$ and $k \geq 1$, let $n = 2r + k + 1$ and $a = 2r + 1$, so $n - a = k$. To a word $u'$ the setting attaches a positive integer $T_{u'}$ and a frame $Y = (e_1, \dots, e_r, z_{u'}, f_1, \dots, f_r)$ of $a$ vectors in $V$; the vectors $e_i, f_i$ do not depend on $u'$. Let $T$ be the Gram matrix of $Y$. At $v$ we rescale the frame: $Y_v$ has $\mathfrak{d}_v^{-(r - i)} e_i$ in place of $e_i$ and $\mathfrak{d}_v^{\,r - i} f_i$ in place of $f_i$, and keeps $z_{u'}$. The rescaled frame has the same Gram matrix $T$ (the *Gram matrix identity*); this holds since the $e_i$ and the $f_i$ are isotropic and $e_i$ and $f_i$ are multiplied by inverse scalars.

**Definition 5.5.2 (Bad places of a word).** A finite place $v$ is *bad* for $u'$ if $v$ divides $T_{u'}$, that is, $T_{u'} \in \mathfrak{p}_v$.

At a bad place the Gram matrix of $Y_v$ reduces modulo a uniformizer to a matrix of corank one, in the sense of condition 4 below: one row and the same column vanish, and adding $1$ at their crossing gives a unit determinant. This is the case where the unimodular formula does not apply.

**Theorem 5.5.3 (Orbit volume at a bad place).** Assume:

1. the standard hypotheses on $E, h, \psi$ (a CM extension, a nondegenerate form, a standard character);
2. $\Lambda$ is an $\mathcal{O}_E$-lattice;
3. the Gram matrix of $Y_v$ is the image of the Gram matrix of the frame;
4. (finite field counts) for every finite field $\mathbb{F}_q$, every $a \leq M$, every nondegenerate Hermitian matrix $J$ of size $M$ over $\mathbb{F}_{q^2}$ and every Hermitian matrix $T$ of size $a$ of corank one (a zero row and column $i_0$, with $T + E_{i_0 i_0}$ invertible),
$$\#\{X \in (\mathbb{F}_{q^2}^M)^a : X \text{ independent}, \ X^* J X = T\} = q^{2 M a - a^2} \prod_{j = M - a}^{M} \big(1 - (-1)^j q^{-j}\big),$$
and the same with $\mathbb{F}_q \times \mathbb{F}_q$ and the swap in place of $\mathbb{F}_{q^2}$ and its Frobenius, with $1$ in place of $-1$.

Let $\psi$ be standard and let $v$ be a bad place for $u'$ such that $\Lambda$ is self-dual at $v$, $v$ is unramified in $E$, and $Y_v$ is primitive in $\Lambda_v$. Then
$$\omega_T(K_v Y_v) = |\mathfrak{d}_v|_v^{\,n a - a^2 / 2} \prod_{j = n - a}^{n} \big(1 - \eta_v^j q_v^{-j}\big).$$

Lean: `PI.OmVg.omVBadT_of_ffX`.

*Proof.* The orbit $K_v Y_v$ is open and compact in its fibre, and its volume is computed by reduction modulo a uniformizer $\varpi$ of $F_v$. The self-dual measure normalizes the volume of $\Lambda_v^a$ to $|\mathfrak{d}_v|_v^{n a}$ and the volume of the Hermitian integral matrices to $|\mathfrak{d}_v|_v^{a^2/2}$, which gives the power of $|\mathfrak{d}_v|_v$. The remaining factor is a ratio of counts. Since $Y_v$ is primitive and $\Lambda_v$ is self-dual, the classes modulo $\varpi$ of the tuples in the orbit are the linearly independent tuples over the residue ring $\mathcal{O}_{E_v} / \varpi$ whose Gram matrix is the reduction of $T$, and the orbit map is an isomorphism of these residue classes onto the fibre classes. The reduction of $T$ has corank one, since $v$ divides $T_{u'}$; this is a computation with the Gram matrix of the frame. When $v$ is inert, $\mathcal{O}_{E_v} / \varpi = \mathbb{F}_{q_v^2}$ with its Frobenius and $\eta_v = -1$; when $v$ splits, it is $\mathbb{F}_{q_v} \times \mathbb{F}_{q_v}$ with the swap and $\eta_v = 1$. The finite field count gives the number of residue classes as $q_v^{2 n a - a^2} \prod_{j = n - a}^{n} (1 - \eta_v^j q_v^{-j})$, and the power of $q_v$ cancels against the volume of one residue class. $\square$

**Theorem 5.5.4 (Orbit volume at a bad place, closed form).** The conclusion of the theorem on bad places holds for every setting, every word $u'$ and every $\psi$.

Lean: `Formalism.L2.SG.Pf.NcVal.OmVSt.OmVZ.omVBadT_holdsX`.

*Proof.* This is the [theorem](/entry/om-vbad-t-of-ff-x/) applied to the standard hypotheses, the lattice property of $\Lambda$, the equality of Gram matrices, and the two finite field counts, all of which hold. The finite field counts are the classical counts of isometric embeddings into a finite unitary space, for a target of corank one. $\square$

### The orbit volume at every place

Let $i_0(v) = k$ if $v$ is bad for $u'$, and $i_0(v) = k + 1$ otherwise, and put
$$\alpha_v(u') = \prod_{i = i_0(v)}^{n} \big(1 - \eta_v^i q_v^{-i}\big).$$

**Theorem 5.5.5 (Orbit volume of a frame).** Let $\psi$ be standard. Then at every finite place $v$, the local orbit volume of the frame of $u'$ is
$$\omega_T(K_v Y) = |\mathfrak{d}_v|_v^{\,n (2r + 1) - (2r + 1)^2 / 2} \, \alpha_v(u'),$$
where $Y$ is the frame of $u'$ and $T$ its Gram matrix.

Lean: `Formalism.L2.SG.Pf.NcX.OmVSt.omVZ_holdsX` (also `Formalism.L2.SG.Pf.NcVal.OmVSt.OmVZ.omV_holdsX`, a second name).

*Proof.* First, the orbit volume of the frame is equal to the orbit volume of $Y_v$ (the *scaling identity*): both orbits lie in the fibre over $T$, by the Gram matrix identity, and the rescaling does not change the self-dual volume of the orbit. Second, in the setting the lattice $\Lambda$ is self-dual at every finite place, $E / F$ is unramified at every finite place, and $Y_v$ is primitive in $\Lambda_v$ for every $v$. If $v$ is bad, the [closed form at a bad place](/entry/om-vbad-t-holds-x/) gives the value, and with $a = 2r + 1$ and $n - a = k$ the product runs from $k$ to $n$. If $v$ is not bad, the determinant of the Gram matrix of $Y_v$ is a unit at $v$, and the unimodular formula gives the value with the product from $n - a + 1 = k + 1$ to $n$. In both cases the product is $\alpha_v(u')$. $\square$

### The typed places

A finite set of places is *typed*: these are the places that divide one of two fixed positive integers $g_0, g_1$, and at such a place let $g_v$ be $g_0$ if $v$ divides $g_0$ and $g_1$ otherwise. At a typed place two volumes enter the counting formula. The first, $\mathrm{vol}_U(v)$, is the self-dual volume of the set of pairs $(x, x')$ of strictly upper triangular coordinates of the unipotent radical that are integral after the rescaling by powers of $\mathfrak{d}_v$, and congruent to each other modulo $g_v$. The second, $\mathrm{vol}_Z(v)$, is the self-dual volume of the set of matrices $z$ of size $r + 1$ such that, after the rescaling, $y = (z - \Theta_u)/g_v$ is integral and $y + y^* - (\Theta_{u'} - \Theta_u)/g_v$ is divisible by $g_v$. Here $\Theta_u, \Theta_{u'}$ are the Gram matrices of the first $r + 1$ vectors $e_1, \dots, e_r, z_u$ of the frames of $u$ and $u'$.

**Theorem 5.5.6 (Typed volume ratio).** Let $\psi$ be standard, and let the integers $T_u, T_{u'}$ satisfy $T_u \equiv T_{u'} \pmod{g_S^2}$, where $g_S = g_0 g_1$. Then at every typed place $v$,
$$\frac{\mathrm{vol}_U(v)}{\mathrm{vol}_Z(v)} = g_v^{(r + 1)(2r + 3)}.$$

Lean: `Formalism.L2.SG.Pf.NcVal.volTypV_holds`.

*Proof.* At a typed place $|\mathfrak{d}_v|_v = 1$, so the rescaling by powers of $\mathfrak{d}_v$ is trivial. The conductor of $\psi_v$ is the inverse different, so the self-dual measure gives volume $1$ to the integral points of $E_v$. The volume of the Hermitian box of level $g_v$ (the integral matrices $y$ of size $r + 1$ with $y_{ij} \equiv c_{ij}$ modulo $g_v$ above the diagonal and $y_{ii} + \bar y_{ii} \equiv c_{ii}$ modulo $g_v$ on it, for an integral Hermitian $c$) is $g_v^{-(r+1)^2}$. The congruence $T_u \equiv T_{u'} \pmod{g_S^2}$ makes the second condition on $z$ a condition of this form in the variable $y = (z - \Theta_u)/g_v$, with $c = (\Theta_{u'} - \Theta_u)/g_v$, which is integral by the congruence. Both $\mathrm{vol}_U(v)$ and $\mathrm{vol}_Z(v)$ are then products of volumes of congruence conditions, coordinate by coordinate, and their quotient is $g_v^{(r+1)(2r+3)}$. $\square$

**Remark 5.5.7 (Formalization).** The fibre family and the self-dual measures are chosen by the axiom of choice, with the zero measure if none exists; their existence and uniqueness are separate statements. The predicate `OmVBadT` is defined twice with the same body, in `NcXOmVSt.lean` (line 51) and in [LocalGramMatrixFrame.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/LocalGramMatrixFrame.lean#L51), and so are `OmVStd`, `OmVLat` and `OmVGram`. The file [OmVBadTHoldsX.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/ValuationLocalVolumes/OmVBadTHoldsX.lean#L28) has two proofs of the orbit volume of a frame: `omV_holds` (line 28) and `omVZ_holdsX` (line 45); `omV_holdsX` (line 57) only renames the second. The proof of the closed form at a bad place uses an isomorphism of residue classes `IsoW` and a reduction statement `RedP`, which we did not unfold beyond the description above. The unimodular formula is `OmLocU`, proved as `PI.OmLocU.Done.omLocU_closed`. The typed ratio is proved through the box volume `VolTHermBox` and the congruence statement `VolTTFCong`; we did not unfold these. The box volume is stated with the integer $g_v$, as $g_v^{-(r+1)^2}$, and not with its absolute value at $v$; we did not check how the arithmetic facts at typed places (`VolUT.typ_arith`) reconcile the two.
