---
title: The sharp E8 class
decls:
  - GlobalTheory.SharpGood.goodClass_sharpClass
  - GlobalTheory.T.isGoodThetaComplexClass_E8Sharp
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The sharp E8 class

This section and the next one connect the theta families of [the section on theta families](/entry/nonempty-theta-fam/) with the Siegel families of [the section on full level models](/entry/top-amp-exists/). The idea is to replace a principally polarized abelian scheme $B$ of dimension $h$ by its eighth power $B^8$, with the polarization twisted by the $E_8$ form. The eighth power has a ring of endomorphisms that contains all integer $8 \times 8$ matrices, and its theta level objects form a class to which the existence theorem for theta families applies. This section defines the *sharp class* of such eighth powers and proves that it is good of dimension $h(h+1)/2$, the dimension of the Siegel space. So [the existence theorem](/entry/nonempty-theta-fam/) gives a theta family for it. [The next section](/entry/exists-is-sharp-of-dense/) shows that the universal object of such a family is an eighth power of a principal Siegel object. The background is [the complex uniformization](/learn/abelian-varieties/#the-complex-uniformization), [Siegel moduli schemes and level structures](/learn/abelian-varieties/#siegel-moduli-schemes-and-level-structures) and [lattices in quadratic and hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

We use the bases of level $k$, the theta level objects and their maps of [the section on theta level objects](/entry/derivation-eq-zero-of-ks-zero/), and the good classes and the sets $S_\mathcal{C}$ of points that come from a class $\mathcal{C}$ of [the section on theta families](/entry/nonempty-theta-fam/). We write $\omega_h$ for the standard symplectic form on $\mathbb{Z}^{h} \oplus \mathbb{Z}^{h}$, so $\omega_h(x, y) = \sum_i (x'_i y''_i - x''_i y'_i)$ for $x = (x', x'')$ and $y = (y', y'')$. We write $\omega_g^{\mathrm{std}}$ for the standard symplectic matrix on $\mathbb{Z}^{2g}$ and $E_{uv}$ for the $8 \times 8$ matrix unit with $1$ at $(u, v)$ and $0$ elsewhere.

### The E8 form and sharp bases

The classical fact behind the construction is the following.

**Theorem 5.17.1 (The E8 lattice).** Up to isomorphism there is exactly one even unimodular positive definite lattice of rank 8, the lattice $E_8$. Every even unimodular positive definite lattice has rank divisible by 8 (J.-P. Serre, *A Course in Arithmetic*, Chapter V, §1 and §2).

A Gram matrix $G$ of $E_8$ is an integer symmetric matrix with even diagonal. Write $G = W + W^{T}$ with $W$ the upper triangular part of $G$, with half of the diagonal on the diagonal of $W$. Then $x^{T} W x = \tfrac12 x^{T} G x$ is the integer quadratic form of the lattice.

**Definition 5.17.2 (E8 matrix).** An integer $8 \times 8$ matrix $W$ is an *E8 matrix* if $W + W^{T}$, seen as a real matrix, is [[positive definite|0QQCG3JWJ4]] and $\det(W + W^{T}) = 1$.

Lean: `GlobalTheory.ZM.IsE8`.

The condition does not say that $W + W^{T}$ is the Gram matrix of $E_8$. It only says that $W + W^{T}$ is an even unimodular positive definite form, since its diagonal entries $2 W_{uu}$ are even. By the theorem above every such form is a Gram matrix of $E_8$. An explicit E8 matrix $W_8$ exists, with $W_8 + W_8^{T}$ the Gram matrix of $E_8$.

**Definition 5.17.3 (Sharp basis).** Let $W$ be an integer $8 \times 8$ matrix and $g, h \ge 0$. A *sharp basis* for $W$ is a linear isomorphism $\mathrm{bas} : \mathbb{Z}^{2g} \to (\mathbb{Z}^{h} \oplus \mathbb{Z}^{h})^{8}$ such that for all $i, j$,
$$
\sum_{u, v} (W + W^{T})_{uv} \, \omega_h\bigl(\mathrm{bas}(e_i)_u, \mathrm{bas}(e_j)_v\bigr) = (\omega_g^{\mathrm{std}})_{ij}.
$$

Lean: `GlobalTheory.ZM.IsSharpBasis`.

So $\mathrm{bas}$ carries the standard symplectic form on $\mathbb{Z}^{2g}$ to the tensor product of the form $W + W^{T}$ with $\omega_h$. Since $\mathrm{bas}$ is an isomorphism, $2g = 16h$, so $g = 8h$.

### Siegel objects and sharp objects

**Definition 5.17.4 (Siegel object).** Let $b$ be a base of level $k$ on $o$, with its unit $\zeta$, and $s : S \to \operatorname{Spec} o$. A *Siegel object* of genus $h$ and level $k$ over $s$ consists of:

1. a commutative abelian scheme $B \to S$;
2. a line bundle $P$ on $B \times_S B$, trivial along $\{1\} \times B$ and along $B \times \{1\}$, with $P \cong \mathrm{sw}^* P$ for the swap $\mathrm{sw}$ of the factors;
3. a map $\mathrm{lev}$ from $\mathbb{Z}^{h} \oplus \mathbb{Z}^{h}$ to the sections of $B$, with $\mathrm{lev}(x + y) = \mathrm{lev}(x)\,\mathrm{lev}(y)$ and $\mathrm{lev}(x)^{k} = 1$.

It must satisfy the following at every geometric point $x : \operatorname{Spec} K \to S$ over $\beta : o \to K$, with $z = \beta(\zeta)$: $\mathrm{lev}(a)$ vanishes at $x$ if and only if $a \in k\,\mathbb{Z}^{2h}$; every $k$-torsion point of $B_x$ is some $\mathrm{lev}(a)$; and the Weil pairing at level $k$ of the diagonal bundle $\Delta^* P$ on $\mathrm{lev}(a)$ and $\mathrm{lev}(b)$ is $z^{2 \omega_h(a, b)}$. The Siegel object is *principal* if $\Delta^* P$ is relatively ample and every section $y$ of $B$ such that $P$ restricted to $\{y\} \times B$ is trivial is $y = 1$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.SiegPre`, `ReciprocityTheory.ChartRestriction.G.Geo.Tor.SiegPre.Principal`.

For a principal Siegel object, $P$ plays the part of the Poincaré bundle pulled back along the polarization $B \to B^\vee$, the polarization is injective, and $\Delta^* P$ is twice the polarization. So $\mathrm{lev}$ is a symplectic level $k$ structure.

**Definition 5.17.5 (Sharp object).** Let $W$ be an integer $8 \times 8$ matrix, $a_j$ ($j \in J$) integer $8 \times 8$ matrices and $\mathrm{bas}$ a linear isomorphism as above. Let $t$ be a theta level object of genus $g$ and level $k$ over $s$, with abelian scheme $A$, line bundle $L$, points $P_1, \dots, P_{2g}$ and endomorphisms $\alpha_j$. Let $c$ be a Siegel object of genus $h$ and level $k$ over $s$ with abelian scheme $B$. Then $t$ is *sharp* over $c$ for $(W, a, \mathrm{bas})$ if there are homomorphisms $\mathrm{pr}_u : A \to B$ ($u = 1, \dots, 8$) such that:

1. the $\mathrm{pr}_u$ identify $A$ with $B^{8}$: for every $T$ over $S$ and maps $y_u : T \to B$ there is exactly one $x : T \to A$ with $\mathrm{pr}_u \circ x = y_u$ for all $u$;
2. $L \cong \bigotimes_{u, v} (\mathrm{pr}_u, \mathrm{pr}_v)^* P^{\otimes W_{uv}}$;
3. $\mathrm{pr}_u \circ \alpha_j = \prod_v \mathrm{pr}_v^{\,(a_j)_{uv}}$ for all $j$ and $u$;
4. $\mathrm{pr}_u \circ P_i = \mathrm{lev}\bigl(\mathrm{bas}(e_i)_u\bigr)$ for all $i$ and $u$.

A complex theta level object $t$ over $\operatorname{Spec} \mathbb{C}$, seen over $o$ through $em : o \to \mathbb{C}$, is in the *sharp class* for $(W, a, \mathrm{bas}, em)$ if there is a principal Siegel object $c$ over the same base with $t$ sharp over $c$.

Lean: `GlobalTheory.ZM.IsSharp`, `GlobalTheory.ZM.SharpClass`.

In words, $A = B^{8}$, the endomorphism $\alpha_j$ acts by the matrix $a_j$, the level points of $t$ are those of $c$ in the coordinates given by $\mathrm{bas}$, and $L$ is the polarization of $B$ tensored with the quadratic form $W$. If $W$ is an E8 matrix, the Riemann form of $L$ is the tensor product of $W + W^{T}$ with the Riemann form of $B$, which is unimodular. So $L$ is a principal polarization, and condition 4 with a sharp basis makes the $P_i$ a symplectic basis.

### The sharp class is good

**Theorem 5.17.6 (The sharp class is good).** Assume the laws, the second laws, the theorem of the cube and the uniformization theorem for complex abelian varieties. Let $h, g \ge 0$, let $W$ be an integer $8 \times 8$ matrix, $J$ a finite set, $a_j$ ($j \in J$) integer $8 \times 8$ matrices, $w, w' \in J$ and $\mathrm{bas} : \mathbb{Z}^{2g} \to (\mathbb{Z}^h \oplus \mathbb{Z}^h)^8$ a linear isomorphism. Assume:

1. $W$ is an E8 matrix and $\mathrm{bas}$ is a sharp basis for $W$;
2. $(W + W^{T})\, a_w = W$ and $(W + W^{T})\, a_{w'} = W^{T}$;
3. for all $u, v$ there is $j \in J$ with $a_j = E_{uv}$.

Then there are integer $2g \times 2g$ matrices $M_j$ ($j \in J$) and an integer $\kappa \ge 0$ such that for every odd prime $n$ there is $j_0$ with the following property. For all $j \ge j_0$, with $N' = n^j$, every ring $o$, every base $b$ of level $N'^2$ on $o$ and every ring map $em : o \to \mathbb{C}$, the sharp class for $(W, a, \mathrm{bas}, em)$ is good of dimension $h(h+1)/2$ for $(M, \kappa, w, w')$.

Lean: `GlobalTheory.SharpGood.goodClass_sharpClass` (also `GlobalTheory.T.isGoodThetaComplexClass_E8Sharp`, a second name).

Condition 2 fixes the unitary pair: $a_w = (W + W^{T})^{-1} W$ and $a_{w'} = (W + W^{T})^{-1} W^{T}$, which exist since $W + W^{T}$ is unimodular.

*Proof.* *The matrices.* Let $M_j$ be the matrix of the map $\mathrm{bas}^{-1} \circ a_j \circ \mathrm{bas}$, where $a_j$ acts on $(\mathbb{Z}^{2h})^8$ by $(x_u)_u \mapsto (\sum_v (a_j)_{uv} x_v)_u$. So the $i$-th column of $M_j$ is $\mathrm{bas}^{-1}\bigl(u \mapsto \sum_v (a_j)_{uv}\, \mathrm{bas}(e_i)_v\bigr)$. This is the action of $\alpha_j$ on the level points, by conditions 3 and 4 of a sharp object.

*Lattices.* Fix an identification of the index sets $\{1, \dots, 2g\}$ and $\{1, \dots, 8\} \times \{1, \dots, 2h\}$ from $\mathrm{bas}$. Let $E$ be the alternating form on $(\mathbb{Z}^{2h})^8$ given by $E(x, y) = \sum_{u, v} (W + W^T)_{uv}\, \omega_h(x_u, y_v)$. For $\tau$ in the Siegel space $\mathfrak{H}_h$ of symmetric complex $h \times h$ matrices with positive definite imaginary part, let $Q_\tau : (\mathbb{Z}^{2h})^8 \to \mathbb{C}^{g}$ send $x$ to the vector with entries $(\tau x'_u + x''_u)_i$ at $(u, i)$. A lemma on tensor lattices states that $Q_\tau$ is injective with discrete image of full rank, that there is a positive definite Hermitian matrix $H_\tau$ with $\operatorname{Im} H_\tau(Q_\tau x, Q_\tau y) = E(x, y)$, and that for each matrix $a$ there is $\kappa_0(a)$ with $L^{\kappa_0(a)} \otimes \alpha^* L^{-1}$ ample for the endomorphism $\alpha$ of $a$. Since $J$ is finite, $\kappa = \max_j \kappa_0(a_j)$ exists. So $\mathbb{C}^g / Q_\tau$ is the complex torus $(\mathbb{C}^h / (\tau \mathbb{Z}^h + \mathbb{Z}^h))^8$ with the polarization $H_\tau$.

*Coordinates.* A lemma on Siegel coordinates gives an open convex set $B \subseteq \mathbb{C}^{d}$, with $d = h(h+1)/2$, and a holomorphic map $\tau : \mathbb{C}^d \to M_h(\mathbb{C})$ such that $\tau(z) \in \mathfrak{H}_h$ for $z \in B$ and every point of $\mathfrak{H}_h$ is $\tau(z)$ for exactly one $z \in B$. The map takes $z$ to the symmetric matrix with entries $z_{\{i, j\}}$.

*The unitary pair.* From condition 2, $(W + W^T)(a_w + a_{w'}) = W + W^{T}$, and $W + W^T$ is invertible, so $a_w + a_{w'} = 1$. A lemma on tensor forms gives $a_w^{T} (W + W^T) = (W + W^T) a_{w'}$, so $a_w$ and $a_{w'}$ are adjoint for $E$.

*Reduction to lattice families.* A lemma on good classes from lattice families gives $j_0$ for each odd prime $n$ and states: a class $\mathcal{C}$ is good of dimension $d$ for $(M, \kappa, w, w')$ if it is closed under isomorphism, every member satisfies the unitary relations and has shape $(M, \kappa)$, every member is the complex torus of some lattice $Q_{\tau(z)}$ with level points and theta values given by uniformization, and conversely the torus of each $Q_{\tau(z)}$, with suitable level points, is a member. The level points of a member are determined modulo $N'^2$ by a homomorphism on $\mathbb{Z}^{2h}$, and there are finitely many such homomorphisms. A lemma on representatives picks one representative of each, and we take one copy of $B$ for each representative. These are the finitely many families $B_1, \dots, B_r$ in the definition of a good class.

*Closure and shape.* A lemma on sharp classes states that the sharp class satisfies the unitary relations for $(w, w')$, has shape $(M, \kappa)$ and is closed under maps of theta level objects over the identity. This uses the matrix $M_j$ above and the bound $\kappa$.

*Members from lattices.* For $\tau \in \mathfrak{H}_h$, let $B_\tau = \mathbb{C}^h / (\tau \mathbb{Z}^h + \mathbb{Z}^h)$ with its principal polarization and its standard level points. A lemma on eighth powers from uniformization states that $B_\tau^8$, with $L$ built from $W$, $\alpha_j$ acting by $a_j$ and level points by $\mathrm{bas}$, is sharp over $B_\tau$. So it is a member of the sharp class.

*Lattices from members.* Conversely, let $t$ be a member, sharp over a principal Siegel object $c$ with abelian variety $B$. By the uniformization theorem, $B = \mathbb{C}^h / \Lambda$ with a symplectic basis of $\Lambda$ for the Riemann form, and $\Lambda = \tau \mathbb{Z}^h + \mathbb{Z}^h$ for a period matrix $\tau \in \mathfrak{H}_h$. A lemma on periods of eighth powers transports this uniformization along $\mathrm{pr}$ to $A = B^8$. The result is the lattice $Q_\tau$, the Hermitian form $H_\tau$ and the theta functions of $L$. Then $\tau = \tau(z)$ for exactly one $z \in B$. The level points of $t$ agree with the chosen representative, by condition 4 and the uniqueness in condition 1.

The lemma on lattice families now gives that the sharp class is good of dimension $d$. $\square$

**Remark 5.17.7.** The first part of the proof is linear algebra over $\mathbb{Z}$: the sharp basis turns the standard symplectic lattice of rank $2g$ into the tensor product of the $E_8$ lattice with the standard symplectic lattice of rank $2h$. The second part is the classical uniformization of principally polarized abelian varieties by the Siegel space. The theorem does not use condition 3, the hypothesis on matrix units; it is needed only in the next section. The matrices $M_j$ and the bound $\kappa$ do not depend on $n$, $o$ or $em$.

**Remark 5.17.8 (Formalization).** The theorem is proved in [IsGoodThetaComplexClassE8Sharp.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/IsGoodThetaComplexClassE8Sharp.lean#L151). The matrix unit hypothesis is introduced as `_` at line 152, so it is not used. The main steps are `GlobalTheory.TensorSiegel.tensor_siegel_lattices`, `GlobalTheory.exists_siegel_coordinates`, `GlobalTheory.T.goodThetaClass_of_lattice_families`, `GlobalTheory.T.sharpClass_prim_and_closed_under_tMap`, `GlobalTheory.T.eighthPower_theta_object_of_uniformisation` and `GlobalTheory.T.exists_periods_eighthPower_evenUnimodularBundle`. We followed the statements of these lemmas and did not open their proofs. The condition `IsE8` does not fix $W + W^T$ as the $E_8$ Gram matrix; the classical theorem makes this harmless, and `GlobalTheory.ZM.isE8_W8` gives an explicit example. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
