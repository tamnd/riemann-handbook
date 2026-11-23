---
title: Unitary data, frames and vectors
decls:
  - UpperTheory.Gal.W2.Seed.SetupEx_holds
  - UpperTheory.Gal.Int.Geo.Pl.datEx_holds
  - UpperTheory.Gal.Int.Geo.Pl.frameEx_holds
  - UpperTheory.Gal.CertificateRingHomMap.seedGU_holds
  - UpperTheory.Gal.Int.Geo.Pl.vecEx_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Unitary data, frames and vectors

Section 07 used plans: for a space $U$ of automorphic forms on a unitary group, a plan gives moduli data, a level, a Hecke eigensystem, a Hecke character and a test function. This section builds the first three ingredients of a plan. An arithmetic datum on the CM field $E$ gives moduli data of the kind of Section 08 at every good prime $p$ (Theorems on setups and data below). A frame identifies the group $G$ of these moduli data, away from $p$, with a unitary similitude group of $E^n$ (Theorem on frames). A vector attached to $U$ is a nonzero algebraic form in $U$ with a type at a split place and a Hecke character that gives its central action (Theorems on seeds and vectors). Sections 15 and 16 use all three.

Throughout, $E$ is a CM field with complex conjugation $c$, and $n \geq 1$ is the rank; in Section 07 the rank was called $a$. For a finite place $w$ of $E$, write $E_w$ for the completion and $\mathcal{O}_w$ for its ring of integers. Let $\mathrm{GU}_n$ be the group of similitudes of the standard hermitian form $\sum_i c(y_i) z_i$ on $E^n$, which is definite at every infinite place; its rational points are taken with positive similitude factor. For $g$ in its group of finite adelic points, write $g_w \in \mathrm{GL}_n(E_w)$ for the component at $w$ and $\mathrm{sim}(g)$ for the similitude factor. A finite place $w$ is *split* if it is split over the maximal totally real subfield $E^+$.

### Arithmetic data and setups

**Definition 3.14.1 (arithmetic datum).** An *arithmetic datum* $A$ on $E$ consists of:

1. an integer $\omega \in \mathcal{O}_E$ with $\omega + c(\omega) = \mathrm{tr} \in \mathbb{Z}$ and $\omega c(\omega) = \mathrm{nm} \in \mathbb{Z}$, such that $\mathrm{tr}^2 - 4\,\mathrm{nm} < 0$;
2. an embedding $\tau_0 : E \to \mathbb{C}$;
3. an element $c_0 \in \mathcal{O}_E$ fixed by $c$, with $\tau_0(c_0) < 0$ and $\tau(c_0) > 0$ for every embedding $\tau$ not inducing the place of $\tau_0$;
4. an element $\delta \in E$ with $c(\delta) = -\delta$, such that $\operatorname{tr}_{E/\mathbb{Q}}(\delta y) \in \mathbb{Z}$ for all $y \in \mathcal{O}_E$, and $\operatorname{Im} \tau(\delta) < 0$ for every $\tau$ with $\tau(\omega) = \tau_0(\omega)$.

A prime $q$ is *good* for $A$ if $q$ does not divide $\mathrm{tr}^2 - 4\,\mathrm{nm}$, the polynomial $X^2 - \mathrm{tr}\, X + \mathrm{nm}$ has a root modulo $q$, and the alternating form below is perfect at $q$ up to a factor prime to $q$.

Lean: `UpperTheory.Gal.W2.Seed.Arith`.

Item 1 says that $\omega$ generates an imaginary quadratic field inside $E$. A good prime splits in this field, as the moduli data of Section 08 need. Let $H = \mathrm{diag}(-c_0, -c_0^2, \dots, -c_0^2)$. By item 3, $H$ has signature $(1, n-1)$ at $\tau_0$ and is definite at the other places. The alternating form $\langle y, z \rangle = \operatorname{tr}_{E/\mathbb{Q}}(\delta\, {}^t c(y) H z)$ on $\mathcal{O}_E^n$ takes integer values by item 4.

**Definition 3.14.2 (setup).** Let $A$ be an arithmetic datum, $n \geq 1$, and $p$ a good prime for $A$. A *setup* for $(A, n, p)$ is a choice of moduli data in the sense of Section 08 with $F = E$, $\mathcal{O} = \mathcal{O}_E$, $m = 1$, lattice $\mathcal{O}_E^n$ with the form $\langle\ ,\ \rangle$, one real place $\tau_0$ of signature one, data at $p$, and a link between these data and a group $G$, such that the link is the identity on $E$ and the action of an integral matrix on the lattice is matrix multiplication.

Lean: `UpperTheory.Gal.W2.Seed.Setup`.

**Theorem 3.14.3 (setups exist).** Let $A$ be an arithmetic datum, $n \geq 1$ and $p$ a good prime for $A$. Then there is a setup for $(A, n, p)$.

Lean: `UpperTheory.Gal.W2.Seed.SetupEx_holds`.

*Proof.* We check the conditions on the moduli data in turn. The form $\langle\ ,\ \rangle$ is alternating since $c(\delta) = -\delta$, it is nondegenerate since $H$ is invertible, and multiplication by $a \in \mathcal{O}_E$ has adjoint multiplication by $c(a)$. It is perfect at $p$ up to a factor prime to $p$ since $p$ is good. The signature condition holds at $\tau_0$ by the computation above, and the sign condition on $\delta$ fixes the orientation of the hermitian form at the places where $\omega$ maps to $\tau_0(\omega)$. The data at $p$ come from the splitting of $p$ in $\mathbb{Q}(\omega)$. The group $G$ is the group of $\mathcal{O}_E$-linear similitudes of the lattice, with its representation on the lattice; the link is then the identity on $E$, and the representation laws and the adjoint law hold by construction. $\square$

**Theorem 3.14.4 (data exist).** Let $\ell$ be a prime, $n$ odd, $d > 0$, and $x \in E$ with $x^2 = -d$, and suppose $(E, \ell, d)$ satisfies the field conditions of Definition 3.7.1. Let $Q$ be a finite set of primes $q$ such that $-d$ is a square in $\mathbb{Q}_q$. Then there is an arithmetic datum $A$ on $E$ such that:

1. $\omega$ and $x$ generate the same subfield of $E$ over $\mathbb{Q}$;
2. every $q \in Q$ is good for $A$;
3. for some $e > 0$, every prime $q \nmid e$ such that $-d$ is a square in $\mathbb{Q}_q$ is good for $A$;
4. for each finite set $X$ of primes there are a prime $p \notin X$ and a setup for $(A, n, p)$ in the standard range of Section 12.

Lean: `UpperTheory.Gal.Int.Geo.Pl.datEx_holds`.

*Proof.* Choose $\tau_0$. We take as given an arithmetic datum $A$ with $\mathbb{Q}(\omega) = \mathbb{Q}(x)$, with $X^2 - \mathrm{tr}\,X + \mathrm{nm}$ split modulo each $q$ at which $-d$ is a square, and good at each $q \in Q$; and an integer $e > 0$ such that the form is perfect at every prime $q \nmid e$ up to a factor prime to $q$. This gives items 1 to 3. For item 4, take a prime $p$ larger than $e$ and than every element of $X$ with $-d$ a square in $\mathbb{Q}_p$; such primes exist by the Chebotarev density theorem. Then $p$ is good by item 3, a setup exists by the last theorem, and it is in the standard range because $n$ is odd and $(E, \ell, d)$ satisfies the field conditions. $\square$

### Frames

**Definition 3.14.5 (frame).** Let $S$ be a setup for $(A, n, p)$ with group $G$. A *frame* for $S$ consists of:

1. a surjective homomorphism $j$ from the finite adelic points of $\mathrm{GU}_n$ to $G(\mathbb{A}_f^p)$, with $j(g) = 1$ if and only if $g_w = 1$ for all $w \nmid p$;
2. matrices $a_w \in \mathrm{GL}_n(E_w)$, integral at almost all $w$ and at all $w$ above good primes, and coordinates $v \mapsto v_w \in E_w^n$ on the lattice tensored with $\mathbb{A}_f^p$, such that $v$ lies in the completed lattice if and only if all $v_w$ are integral, the coordinates are surjective onto integral vectors, they are the identity on $\mathcal{O}_E^n$, and $j(g)$ acts as $a_w g_w a_w^{-1}$ in the coordinates at $w$;
3. a map of rational adeles to $\mathbb{A}_f^p$ under which the similitude of $j(g)$ is the image of $\mathrm{sim}(g)$;
4. a definite form $B$ of $G$ in the sense of Section 12, trivial in the adelic sense, whose group of rational points is the group of rational points of $\mathrm{GU}_n$, such that the embedding of this group into $G(\mathbb{A}_f^p)$ is $j$ and its component at $p$ is integral exactly when the components of the rational point at the places above $p$ are integral;
5. the automorphism $\vartheta$ of $\mathrm{GU}_n$ with matrix ${}^t g^{-1}$ and similitude $\mathrm{sim}(g)^{-1}$.

Lean: `UpperTheory.Gal.Int.Geo.Pl.Frame`.

A frame lets us move functions on $\mathrm{GU}_n(\mathbb{A}_f)$ to Hecke functions on $G(\mathbb{A}_f^p)$ and back. The transpose inverse $\vartheta$ turns a form on $\mathrm{GU}_n$ into a form for the dual weight, which is the weight that appears in Hodge cohomology.

**Theorem 3.14.6 (frames exist).** Let $S$ be a setup for $(A, n, p)$ with $n$ odd. Then $S$ has a frame.

Lean: `UpperTheory.Gal.Int.Geo.Pl.frameEx_holds`.

*Proof.* The group $G$ of the setup is the group of $\mathcal{O}_E$-linear similitudes of $(\mathcal{O}_E^n, \langle\ ,\ \rangle)$, and $\langle\ ,\ \rangle$ is the trace of the hermitian form $\delta H$. So an $E$-linear map preserves $\langle\ ,\ \rangle$ up to a rational factor if and only if it preserves $H$ up to the same factor, and $G$ is the similitude group of $H$, or of $-c_0^{-1} H = \mathrm{diag}(1, c_0, \dots, c_0)$. Since $n$ is odd, the determinant $c_0^{n-1}$ of this form is a square. Hermitian forms over a local field are classified by rank and determinant modulo norms, so at each finite place this form is isometric to the standard form, and its similitude group is isomorphic to that of $\mathrm{GU}_n$. Taking the components away from $p$ gives $j$, its kernel and the similitude law. At each $w \nmid p$ the completed lattice is $\mathcal{O}_w^n$ after a change of basis $a_w$, which is integral where $H$ is a unit, so at almost all $w$ and at the good primes. The standard form, carried to $G$ by these isomorphisms, is a definite form $B$ whose group of rational points is that of $\mathrm{GU}_n$. $\square$

### Vectors

For a split place $w_0$, an *$\ell$-type* of $U$ at $w_0$ is an open compact torsion-free subgroup $J \subseteq \mathrm{GL}_n(E_{w_0})$ with a surjection $\theta$ onto $\mathbb{Z}/\ell^m$ and a nontrivial character $\chi$ of $\mathbb{Z}/\ell^m$, such that every smooth irreducible representation of $\mathrm{GL}_n(E_{w_0})$ with a nonzero vector on which $J$ acts by $\chi \circ \theta$ is cuspidal, and $U$ contains a nonzero form on which $J$ acts by $\chi \circ \theta$. This is the type condition at $w_0$ of Definition 3.7.1.

**Definition 3.14.7 (vector).** Let $d > 0$, $x \in E$ with $x^2 = -d$, $U$ an automorphic space on $\mathrm{U}(n)$, $w_0$ a split place, and $\mathrm{Up}$ a set of split places that contains $w_0$ and one place of each pair $\{w, c(w)\}$. A *vector* for $(x, U, w_0, \mathrm{Up})$ consists of:

1. an automorphic representation $\pi$ with space $U$ and an algebraic weight $W = (W_{v,i})$ with nonzero finite part of $\pi$ in weight $W$, integers $m_v \ge 0$ with $W_{v,i} + m_v \geq 0$, and $j_z = \sum_v (\sum_i W_{v,i} + n m_v)$;
2. an open compact torsion-free subgroup $J \subseteq \mathrm{GL}_n(E_{w_0})$ with a character $\chi$ of open kernel such that every smooth irreducible representation with a $\chi$-eigenvector of $J$ is cuspidal;
3. a finite set $S$ of places containing $w_0$, with open compact subgroups $K_w$ for $w \in S$, $K_{w_0} = J$, $K_w \subseteq \mathrm{GL}_n(\mathcal{O}_w)$ for $w \ne w_0$, split places of $S$ in $\mathrm{Up}$ with conjugates outside $S$, and the level group $\prod_{w \in S} K_w$ open and compact;
4. a nonzero function $\Phi$ on $\mathrm{GU}_n(\mathbb{A}_f)$ with values in the dual of the weight space, left equivariant under the rational points through the weight $(W, j_z)$, right equivariant under the level by $\chi$ at $w_0$, and a Satake vector with the parameters of $U$ at the split places $w$ with $w, c(w) \notin S$;
5. an algebraic Hecke character $\kappa$ of $E$ with infinity type determined by $(x, W, j_z)$, unramified away from the places related to $S$, through which the centre acts on $\Phi$ by $\kappa(w)^{-1}$;
6. the condition that every split place $w$ apart from $w_0$ at which $U$ has Satake parameters lies outside $S$ together with $c(w)$.

Its *weight* is $\lambda_{\tau,i} = m_v$ if $\tau$ is the chosen embedding of the place $v$, and $W_{v,i} + m_v$ otherwise.

Lean: `UpperTheory.Gal.Int.Geo.Pl.Vec`.

A vector is the automorphic input of a plan: $\Phi$ is an algebraic modular form with the Hecke eigenvalues of $U$ outside $S$, and $\kappa$ removes the central character.

**Theorem 3.14.8 (seeds of vectors).** Let $n > 0$, $d > 0$, $x^2 = -d$, $\pi$ an automorphic representation with nonzero finite part in weight $W$, $j_z \in \mathbb{Z}$, $\mathrm{Up}$ as above with $w_0 \in \mathrm{Up}$ split, and $J \subseteq \mathrm{GL}_n(E_{w_0})$ open compact with a character $\chi$ such that $U$ contains a nonzero form on which $J$ acts by $\chi$. Then there are $S$, $(K_w)$, $\Phi$ and $\kappa$ that satisfy items 3 to 6 of the definition of a vector, with $K_{w_0} = J$ and $\chi$ of open kernel.

Lean: `UpperTheory.Gal.CertificateRingHomMap.seedGU_holds`.

*Proof.* There is a continuous central embedding $\zeta$ of the finite ideles of $E$ into $\mathrm{GU}_n(\mathbb{A}_f)$ that sends $k \in E^\times$ to a rational scalar matrix and is trivial or integral at the places not related to $x$. We take as given that $S$ and $(K_w)$ with the shape of item 3 and the condition of item 6 exist, together with a nonzero algebraic form $f$ in the finite part of $\pi$ in weight $W$ on which the level acts by $\chi$ at $w_0$; at the split places outside $S$ the form is spherical by item 6, and the kernel of $\chi$ is open because $\chi$ is a smooth character. From $f$ we build $\Phi$ with the equivariance of item 4 and a character $\psi$ of the finite ideles such that $\Phi(g \zeta(y)) = \psi(y) \Phi(g)$. The character $\psi$ is trivial on $E^\times$ up to the algebraic factor of the weight, so it is the finite part of an algebraic Hecke character, and $\kappa$ is its inverse with the infinity type of item 5. The level group is open and compact as a product of open compact groups at the places of $S$ and maximal compact groups elsewhere. $\square$

**Theorem 3.14.9 (vectors exist).** Let $n > 0$, $d > 0$, $x \in E$ with $x^2 = -d$, $U$ an automorphic space on $\mathrm{U}(n)$, $w_0$ a split place such that $U$ has an $\ell$-type at $w_0$, and $\mathrm{Up}$ as above with $w_0 \in \mathrm{Up}$. Then there is a vector for $(x, U, w_0, \mathrm{Up})$.

Lean: `UpperTheory.Gal.Int.Geo.Pl.vecEx_holds`.

*Proof.* Let $\pi$ be the automorphic representation with space $U$. It has a weight $W$ with nonzero finite part. Put $m_v = \sum_i |W_{v,i}|$, so $W_{v,i} + m_v \ge 0$, and $j_z = \sum_v (\sum_i W_{v,i} + n m_v)$. The $\ell$-type gives $J$ and the character $\chi \circ \theta$, with the cuspidality condition of item 2. [Theorem 3.14.8](/entry/seed-gu-holds/) with this $J$, $\chi \circ \theta$ and $j_z$ gives $S$, $(K_w)$, $\Phi$ and $\kappa$. $\square$

**Remark 3.14.10 (Formalization).** `SetupEx_holds` is `pSetupEx` applied to nine facts (`FormOKSt_holds`, `FormPerfSt_holds`, `SigSt_holds`, `DomSt_holds`, `AtPEx_holds`, `RepEx_holds`, `RepLaws_holds`, `RepAdj_holds`, `Orient_holds`), which we did not open; the proof above follows their names. `datEx_holds` is `datEx_of` applied to a prime-existence statement, `ArithK_holds`, `SetupEx_holds`, `ScOf_holds` and `PerfCof_holds`; we opened `datEx_of` but not the inputs, so the facts on $A$ and $e$ are taken as given. `frameEx_holds` builds the transfer `T` from `trEx_holds`, the coordinates from `vecCoord_holds` and the definite form from `pStdForm2`; the local classification argument above is the standard one and is not read from these proofs. A second, unrelated declaration named `frameEx_holds` is in `Development/AbelianVarietyTheory/Proofs/DivisorProofs/CartanEigenOrthonormalFrameExists.lean`. `seedGU_holds` is `seedGU_of` applied to `zetaEx_holds`, `vecU_holds`, `sphType_holds`, `formGU_holds`, `kapOf_holds`, `levOpen_holds` and `levCompact_holds`, and `vecEx_holds` is `vecEx_of seedGU_holds wtAt_holds`. The $\ell$-type is `GlobalTheory.CongW.TyEll`.
