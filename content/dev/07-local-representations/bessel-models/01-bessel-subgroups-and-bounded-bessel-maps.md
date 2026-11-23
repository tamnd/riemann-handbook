---
title: Bessel subgroups and bounded Bessel maps
decls:
  - CompanionTheory.Bmu.bounded
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bessel subgroups and bounded Bessel maps

This section sets up the local objects of the chapter at the real place: a unitary group $G \cong \mathrm{U}(r+k, r+1)$, its Bessel subgroup $R = U_W N$, a generic character of $N$, and Bessel maps from a unitary representation of $G$ to a representation of $U_W$. It then proves that a Bessel map is bounded on each orbit of a smooth vector. The uniqueness theorem of the next section uses this bound, through [Theorem 6.2.7](/entry/bessel-map-uniq-gap/), and that uniqueness is the input from the real place for [HypsAlt is nonempty](/step/nonempty-hyps/). For the global meaning of Bessel periods, see [Bessel and Fourier-Jacobi periods](/learn/periods/#bessel-and-fourier-jacobi-periods) and [local multiplicity one](/learn/periods/#local-multiplicity-one).

### The group

Fix integers $k \geq 1$ and $r \geq 0$, and put $n = 2r + k + 1$. We index coordinates of $\mathbb{C}^n$ by $0, \dots, n-1$ and write $e_0, \dots, e_{n-1}$ for the standard basis.

**Definition 6.1.1 (The Hermitian form $H_{k,r}$).** Let $H = H_{k,r}$ be the $n \times n$ matrix with these entries. For $a < r$, the entries $(a, 2r+k-a)$ and $(2r+k-a, a)$ are $1$. For $r \leq i < r+k$, the entry $(i,i)$ is $1$. The entry $(r+k, r+k)$ is $-1$. All other entries are $0$. Put $\langle v, w \rangle_H = w^* H v$ and
$$G = \mathrm{U}(H) = \{ g \in M_n(\mathbb{C}) : g^* H g = H \}.$$

The vectors $e_a$ and $e_{2r+k-a}$ with $a < r$ span $r$ hyperbolic planes. The middle block $W_0 = \mathrm{span}(e_r, \dots, e_{r+k})$ has signature $(k, 1)$. So $H$ has signature $(r+k, r+1)$, and $G \cong \mathrm{U}(r+k, r+1)$ ([unitary groups](/learn/groups/#unitary-groups)). Also $H^2 = 1$. The Lie algebra of $G$ is $\mathfrak{g} = \{ X : X^* H + H X = 0 \}$.

**Definition 6.1.2 (The Bessel data).** Let $z \in W_0$, that is, $z_i = 0$ unless $r \leq i \leq r+k$, and put $T_z = -\mathrm{Re}\,\langle z, z \rangle_H$. We assume $T_z > 0$. Let
$$U_W = \{ g \in G : g e_a = e_a,\ g e_{2r+k-a} = e_{2r+k-a} \text{ for } a < r,\ g z = z \}.$$
Let $N$ be the set of $g \in G$ such that, for each $a < r$, the column $g e_a$ has entry $1$ in row $a$ and entry $0$ in each row $i > a$, and such that $g_{ij} = \delta_{ij}$ for all $i \geq r$ and $r \leq j \leq r+k$.

So $N$ is the unipotent radical of the parabolic subgroup that fixes the isotropic flag $\langle e_0 \rangle \subset \langle e_0, e_1 \rangle \subset \dots \subset \langle e_0, \dots, e_{r-1} \rangle$, and it acts trivially on $W_0$ modulo this flag ([parabolic subgroups](/learn/groups/#parabolic-subgroups)). The group $U_W$ is the unitary group of the orthogonal complement of the hyperbolic planes and of $z$: a group $\mathrm{U}(k)$, since $z$ is a negative vector in $W_0$. It normalizes $N$, and $R = U_W N$ is the Bessel subgroup of the Gan-Gross-Prasad setting.

**Definition 6.1.3 (Generic characters).** For $g \in G$ and $a < r$ put $\ell_a(g) = g_{a, a+1}$ if $a + 1 < r$, and $\ell_{r-1}(g) = (g z)_{r-1}$. For $c = (c_0, \dots, c_{r-1}) \in \mathbb{C}^r$ put
$$\psi_c(g) = \exp\Big( i \, \mathrm{Re} \sum_{a < r} c_a \ell_a(g) \Big).$$
The *standard character* is $\psi_{\mathrm{std}}(g) = \exp\big( i\,\mathrm{Re}\,( -2i \sum_a \ell_a(g) ) \big)$, the case $c_a = -2i$ for all $a$.

On $N$, each $\ell_a$ is additive, so $\psi_c$ is a unitary character of $N$, and it is fixed by conjugation by $U_W$. If all $c_a \neq 0$, then $\psi_c$ is generic in the sense of [generic characters](/learn/periods/#generic-characters): it is nontrivial on each simple root group of the flag and on the last step towards $z$.

### Smooth vectors and Bessel maps

Let $\sigma$ be a unitary representation of $G$ on a Hilbert space $\mathcal{H}$ ([representations of a group](/learn/representations/#representations-of-a-group)). A vector $v$ is *smooth* if $g \mapsto \sigma(g) v$ is smooth. For $X \in \mathfrak{g}$ and smooth $v$ put $d\sigma(X) v = \frac{d}{dt} \sigma(\exp tX) v |_{t=0}$, and for a word $w = (X_1, \dots, X_m)$ in $\mathfrak{g}$ put $d\sigma(w) = d\sigma(X_1) \cdots d\sigma(X_m)$.

**Definition 6.1.4 (Bessel map).** Let $\pi$ be a representation of $U_W$ on a finite-dimensional inner product space $V$, and $\psi$ a function on $N$. A *Bessel map* of type $(\psi, \pi)$ is a map $B : \mathcal{H} \to V$ such that:

1. $B$ is additive and $\mathbb{C}$-linear on smooth vectors;
2. there are a constant $C$ and finitely many words $w_1, \dots, w_s$ in $\mathfrak{g}$ with $\| B v \| \leq C \sum_j \| d\sigma(w_j) v \|$ for all smooth $v$;
3. $B(\sigma(hm) v) = \psi(m)\, \pi(h) B(v)$ for $h \in U_W$, $m \in N$ and smooth $v$.

Condition 2 says that $B$ is continuous on the smooth vectors for a Sobolev norm ([Sobolev norms](/learn/analysis/#sobolev-norms)). A Bessel map is the same as an element of $\mathrm{Hom}_R(\sigma^\infty, \pi \otimes \psi)$, which is the local Bessel model space of Gan, Gross and Prasad, with $\pi$ in place of $\bar\sigma$ in their notation.

### Boundedness on orbits

**Theorem 6.1.5 (Bessel maps are bounded on orbits).** Let $k \geq 1$, let $\sigma$ be a unitary representation of $G$ on a Hilbert space $\mathcal{H}$, let $z \in W_0$ with $T_z > 0$, and let $c \in \mathbb{C}^r$ with $c_a \neq 0$ for all $a$. Let $\pi$ be a map from $G$ to the operators on a finite-dimensional inner product space $V$, with $\pi(1) = 1$, isometric and continuous on $U_W$. Let $B$ be a Bessel map of type $(\psi_c, \pi)$. Then for each smooth $w \in \mathcal{H}$ there is $K$ with
$$\| B(\sigma(g) w) \| \leq K \quad \text{for all } g \in G.$$

Lean: `CompanionTheory.Bmu.bounded`.

*Proof.* The proof has three parts.

First, a decomposition of $G$. There is a matrix $\Gamma$ adapted to $(z, H)$: it carries a fixed Hermitian form $H_q$ of the same signature to $H$, with a diagonal torus that is split. By the Iwasawa, Levi and Cartan decompositions of $\mathrm{U}(H_q)$ ([[Iwasawa decomposition|ZYVEVYBA41]], [reductive groups and maximal compact subgroups](/learn/groups/#reductive-groups-and-maximal-compact-subgroups)), each $g \in G$ is a product
$$g = h \, m \, \Gamma \, d \, R,$$
with $h \in U_W$, $m \in N$, $d$ a positive diagonal matrix of a fixed torus shape, and $R$ unitary. Since $\pi(h)$ is an isometry and $|\psi_c(m)| = 1$, we get $\| B(\sigma(g) w) \| = \| B(\sigma(\Gamma d R) w) \|$. So it is enough to bound $B$ on the set $\{\Gamma d R\}$.

Second, a quotient bound. Choose elements $X_j$ of the Lie algebras of $U_W$ and $N$ and elements $Q_i$ that together span $\mathfrak{g}$. On $\exp(t X_j)$, the map $B$ transforms by $\pi$ or by $\psi_c$. A local chart of $G$ by products of the $\exp(t X_j)$ and condition 2 bound $B(\sigma(g) w)$ by a constant times a finite sum of norms $\| d\sigma(w') \sigma(g) w \|$, where $w'$ runs over words in the $Q_i$ only. Moving these words through $\sigma(g)$ turns them into words in $g^{-1} Q_i g$, of norm at most $C_0 M^c$ when $M$ bounds the ratios of $d$.

Third, the torus. Let $d = \mathrm{diag}(d_0, \dots, d_{n-1})$ and let $M = \max(1, \max_a d_a / d_{a+1})$, the maximum over the simple ratios along the flag. A torus bound gives $\| (dR)^{-1} A (dR) \| \leq n^2 \| A \| M^n$ for each $A$ that vanishes on the upper positions. If $M = 1$, all conjugates $g^{-1} Q_i g$ are bounded and the quotient bound gives a uniform $K$. If $M > 1$, a root vector gives the second case. For the index $a$ with $d_a/d_{a+1} = M$ there is $Y \in \mathfrak{g}$ with $\| Y \| \leq C_0$ and
$$\Gamma d R \exp(\tau Y) (\Gamma d R)^{-1} \in N, \qquad \psi_c\big( \Gamma d R \exp(\tau Y) (\Gamma d R)^{-1} \big) = e^{i (d_a / d_{a+1}) \tau},$$
because $c_a \neq 0$. So $B(\sigma(g \exp \tau Y) u) = e^{i M \tau} B(\sigma(g) u)$. Differentiating in $\tau$ gives $i M \, B(\sigma(g) u) = B(\sigma(g) d\sigma(Y) u)$. Each factor $M$ that the conjugated words cost is paid by one such derivative. This is integration by parts against the oscillating character. The bound on $B(\sigma(g) w)$ is then uniform in $M$. $\square$

**Remark 6.1.6.** The theorem needs no irreducibility and no assumption on the type of $\sigma$. The genericity of $\psi_c$, that is $c_a \neq 0$ for all $a$, is what makes the root vector argument work. For $c = 0$, a Bessel map can grow along the torus.

**Remark 6.1.7 (Formalization).** The theorem takes no discrete series or irreducibility hypothesis ([BesselMapUniqGap.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGap.lean#L240)). The map $\pi$ is a function on all matrices; only its values on $U_W$ enter. The decompositions, the chart, the quotient bound and the root vectors are separate proved statements. They are passed in from wrappers in a folder named `StableLattices` of an unrelated part of the development ([BesselMapUniqGapAlt.lean](lean:CompanionTheory/AutomorphicTheory/BesselOrbitBounds/BesselMapUniqueness/BesselMapUniqGapAlt.lean#L27)). We have not unfolded the adapted matrix $\Gamma$ or the torus shape beyond what is said above.
