---
title: Bessel periods and a realised theta datum
decls:
  - GlobalTheory.T.definiteBesselPeriod_sesquilinear
  - GlobalTheory.RootExch.PosLinear.posLin
  - GlobalTheory.Mem.TrueRecordEq.realisesE
  - GlobalTheory.Mem.TrueRecordEq.exists_realisedE
  - GlobalTheory.Mem.Th.exists_allTied_eqTied_on
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Bessel periods and a realised theta datum

A theta datum collects the spaces, the cusp forms, the Petersson forms, the Weil representations, the theta lifts and the Bessel periods that the iterated construction uses. In this section we first prove that the Bessel period of a definite space, after the root exchanges, is a sesquilinear form that does not depend on the choices of measures, fundamental domains and sections. Then we use it to build a theta datum that realises a given record of functions, and from it a theta datum whose ties all hold. The last result feeds the theta datum on the true rows and columns of the next section.

### Bessel data and position data

Let $E/F$ be the CM extension of the host, with adeles $\mathbb{A}_F$ and $\mathbb{A}_E$. For a Hermitian space $V$ over $E$ we write $G_V(\mathbb{A})$ for the adelic points of its unitary group (see [unitary groups](/learn/groups/#unitary-groups) and [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups)).

**Definition 1.9.1 (Bessel datum).** Let $A$ and $B$ be Hermitian spaces over $E$ and let $\iota : A \to B$ be an isometric embedding. A Bessel datum on $\iota$ consists of an integer $\rho \geq 0$ with $\dim B = \dim A + 2\rho + 1$, isotropic vectors $e_0, \dots, e_{\rho-1}$ and $f_0, \dots, f_{\rho-1}$ in $B$ with $h(e_i, f_j) = \delta_{ij}$, a vector $z$ orthogonal to all $e_i$, all $f_i$ and to $\iota(A)$ with $h(z,z) \neq 0$, and a scalar $\theta \neq 0$. Put $a = (e_0, \dots, e_{\rho-1}, z)$. The unipotent group $N$ is the closure in $G_B(\mathbb{A})$ of the elements that fix the flag of the $e_i$ and act trivially on $\iota(A)$, and $N_\mathbb{Q} = N \cap G_B(F)$. The character of $N$ is
$$\psi_N(n) = \psi\Big(\mathrm{Tr}_{\mathbb{A}_E/\mathbb{A}_F}\Big(\theta \sum_{i < \rho} h(n\, a_{i+1}, f_i)\Big)\Big),$$
for an additive character $\psi$ of $\mathbb{A}_F/F$.

The Bessel datum is the standard input for the Gross-Prasad periods of unitary groups. The vectors $e_i$, $f_i$ span a split part of $B$, and the character $\psi_N$ is generic on the root groups of $N$.

**Definition 1.9.2 (Unit pair and Bessel period).** A unit pair $(\nu, \mathcal{N})$ is a Haar measure $\nu$ on $N$ and a fundamental domain $\mathcal{N}$ for $N_\mathbb{Q}$ in $N$ with $\nu(\mathcal{N}) = 1$ (see [Haar measure](/learn/analysis/#haar-measure)). For a function $F$ on $G_B(\mathbb{A})$ the Bessel coefficient is
$$\mathcal{B}F(g) = \int_{\mathcal{N}} F(ng)\, \overline{\psi_N(n)}\, d\nu(n).$$
Let $(\mu, \mathcal{F})$ be a volume pair for $A$: a Haar measure on $G_A(\mathbb{A})$ and a fundamental domain $\mathcal{F}$ for $G_A(F)$. Let $s : G_A(\mathbb{A}) \to G_B(\mathbb{A})$ be the section of $\iota$, so that $s(h)$ acts as $h$ on $\iota(A)$. The Bessel period of $\varphi$ on $G_A(\mathbb{A})$ and $F$ on $G_B(\mathbb{A})$ is
$$P(\varphi, F) = \int_{\mathcal{F}} \varphi(h)\, \mathcal{B}F(s(h))\, d\mu(h).$$

The period is computed after a finite sequence of root exchanges. For a split idempotent $\varepsilon$ of $\mathbb{A}_E$ and an index $i$, the exchange subgroup $\mathrm{Ex}(\varepsilon, i)$ is a unipotent subgroup of $G_B(\mathbb{A})$, and for a Haar measure $m$ on it the exchange of a functional $b$ is
$$\mathrm{exch}(b)(F) = \int_{\mathrm{Ex}(\varepsilon, i)} b(R(u)F)\, dm(u),$$
with $R$ the right translation.

**Definition 1.9.3 (Position datum).** A position datum on $\iota$ is a Bessel datum together with a number $n$ of moves and, for each move $a < n$, a split idempotent $\varepsilon_a$, an index $p_a$ with $1 \leq p_a \leq \rho + 1$, and Haar measures on the exchange subgroups. The idempotents of different moves are apart: $(\varepsilon_a + \bar\varepsilon_a)(\varepsilon_b + \bar\varepsilon_b) = 0$ for $a \neq b$. The period of the position datum is the Bessel period after the moves: move $a$ applies the exchanges for $\varepsilon_a$ at all indices $i \geq p_a$. The symmetric position datum has $n = 0$, and its period is the Bessel period itself.

Two analytic facts come with the definition. The first says that the period converges absolutely for all right translates of $F$, when $\varphi$ and $F$ are automorphic and $A$ is definite. The second says that, for $i \geq 1$, the partial exchanges are locally constant and of compact support as functions on $\mathrm{Ex}(\varepsilon, i)$, so that each exchange integral is a finite sum.

### Sesquilinearity

**Theorem 1.9.4 (Bessel periods on a definite space).** Both facts above hold. Let $\theta$ be the infinity family, let $\psi$ be the standard character of sign $-1$, let $A$ and $B$ be Hermitian spaces with an embedding $\iota : A \to B$, and let $P$ be a position datum on $\iota$. Assume that $A$ is definite and has admissible signature. Then there is a map $b$ on pairs $(\varphi, F)$, with $\varphi$ an automorphic form on $A$ and $F$ a cusp form on $B$ of type $\theta$, which is conjugate linear in $\varphi$ and linear in $F$, such that
$$P(\bar\varphi, F) = b(\varphi, F)$$
for every volume pair $(\mu, \mathcal{F})$ of $A$, every unit pair $(\nu, \mathcal{N})$ and every section $s$ of $\iota$.

Lean: `GlobalTheory.RootExch.PosLinear.posLin` (also `GlobalTheory.T.definiteBesselPeriod_sesquilinear`, a second name).

*Proof.* Convergence for definite $A$ is a result of the Bessel convergence chapter. For finiteness, the partial exchange of the period at an index $i + 1$ is the exchange of a functional that is fixed by an open compact subgroup and is equivariant under $\psi_N$. A functional of this kind is locally constant on $\mathrm{Ex}(\varepsilon, i)$ and has compact support there, since $\psi$ is standard and $\varepsilon$ is split. This gives the two facts.

Now fix $A$, $B$, $\iota$ and $P$. If there is no volume pair, no unit pair or no section, the identity is empty and we take $b = 0$. Otherwise fix one choice $(\mu, \mathcal{F}, \nu, \mathcal{N}, s)$ and put
$$b(\varphi, F) = \big(\mathrm{move}_P\, \Pi_{\bar\varphi, F}\big)(1), \qquad \Pi_{\bar\varphi,F}(g) = P(\bar\varphi, R(g)F).$$
The function $\Pi_{\bar\varphi, F}$ is linear in $F$ and in $\bar\varphi$, it has a level, and it is equivariant for each $\varepsilon_a$. The exchanges are linear on such functions, and they keep the level and the equivariance, because the idempotents of the moves are apart. So $\mathrm{move}_P$ is additive on the functions $\Pi$, and $b$ is conjugate linear in $\varphi$ and linear in $F$. The convergence fact makes the sums of integrals equal the integrals of sums.

It remains to show that $b$ does not depend on the choices. The section $s$ is unique, since an element of $G_B(\mathbb{A})$ that acts as $h$ on $\iota(A)$ and fixes its complement is determined by $h$. The Haar measure $\mu$ of a volume pair is unique for a space of admissible signature. Two fundamental domains for $G_A(F)$ give the same integral of a left invariant function, and two unit pairs give the same Bessel coefficient, since $F$ is left invariant under $N_\mathbb{Q}$ and $\psi_N$ is trivial on $N_\mathbb{Q}$. So $\Pi$ does not depend on the choices, and the period of $P$ at $(\bar\varphi, F)$ is $b(\varphi, F)$. $\square$

### A realised theta datum

**Definition 1.9.5 (Record of functions).** Let $\theta$ be the infinity family and $\psi$ the standard character of sign $-1$. A record of functions consists of the row maps from multiplicity spaces into cusp forms, the column maps, the Schwartz functions $\Phi$ of the theta kernels, the characters of the rows and the character $\eta$, the multiplicities $m_Y$, the Petersson constants, the measures and the position data of the Bessel periods. A theta datum realises a record of functions, together with a Weil function $W_f$ and a tower of spaces, if its ties hold and each of its objects evaluates to the object of the record with the same name: its automorphic forms are the smooth automorphic functions of type $\theta$, its characters are the characters of the record, its spaces are those of the tower, its theta lifts are the theta integrals of $W_f$ when the pair is admissible and $0$ otherwise, and its Bessel periods are the periods of the record.

**Theorem 1.9.6 (A realised theta datum).** Assume that the Petersson integrals, the top integrals and the Bessel integrals converge, and that the theta lifts are automorphic and agree with the integral formula. Let $\theta$ be the infinity family, $\psi$ the standard character of sign $-1$, $W_f$ a Weil function of equal rank, $T$ a tower of spaces and $R$ a record of functions. Then there is a theta datum $X$ with a theta tie, a Weil tie with character $\psi$ and a Bessel tie which realises $R$, $W_f$ and $T$.

Lean: `GlobalTheory.Mem.TrueRecordEq.exists_realisedE` (also `GlobalTheory.Mem.TrueRecordEq.realisesE`, the proof that the datum realises the record).

*Proof.* We build $X$ from $R$. The spaces are those of $T$. The automorphic forms on a space $V$ are the smooth automorphic functions of type $\theta$, and the cusp forms are those among them that are cuspidal. The Petersson form on $V$ is the integral over a fundamental domain, scaled by the Petersson constant of $R$, and it converges by the first assumption. The theta lift from $V$ to $V'$ is the integral of the theta kernel of $W_f$ against $F$, scaled by the same constant, when the pair is admitted and the signature of $V$ is admissible, and $0$ otherwise. It is automorphic by the fourth assumption. The Bessel period of a position datum is the period of the previous theorem, scaled by the Petersson constant, with the normalising constant $1$ for the Bessel factor. Each tie and each clause of realisation then holds by the construction, by the convergence assumptions, and by the previous theorem for the Bessel clauses. $\square$

**Theorem 1.9.7 (A theta datum with all ties).** Assume the following results from the literature: the existence of the Weil representation for a unitary dual pair, rapid decay of cusp forms, existence and uniqueness of the discrete series of $U(J)$ for each Harish-Chandra parameter, and existence of a discrete series representation with each parameter for the groups $U(p,q)$. Let $C$ be a character frame, $\xi$ a family of Hecke characters on the tuples, and $U$ a set of tuples. Assume that the real places are tied, and that for each $\theta$, $\psi$ and $W_f$ as above there is a record of functions $R$ with characters $C$ and $\xi$, whose rows are tied to $W_f$, and whose row maps are isometric on $U$:
$$\int_{\mathcal{F}} \overline{R_{\mu, j}x(h)}\; R_{\mu, j}y(h)\, d\mu(h) = \frac{\langle x, y\rangle}{m_Y(\mu, j)\, c(Y_j)}$$
for $\mu \in U$, $j \leq m$ and $x, y$ in the multiplicity space. Then there is a theta datum $X$ whose rows are tied to the theta lifts, whose row maps are isometries for the Petersson form on $U$, and which carries a provision $A$ and a complete tie $a$ with Weil and theta compatibility. For each choice $n$ and each tied tuple datum with characters $\xi$, the characters of $a$ agree with those of a tied theta character datum of $X$.

Lean: `GlobalTheory.Mem.Th.exists_allTied_eqTied_on`.

*Proof.* The discrete series results give additive types at the real places. The Weil representation gives a Weil function of equal rank for each standard $\psi$. A tower of spaces exists. Rapid decay gives the five convergence and automorphy assumptions of the previous theorem, so a realised theta datum exists for each record. A provision with the compatibility conditions exists, and the real places give a tied record. With these inputs, the theorem of realisation from the earlier chapter on tied theta data gives $X$, the ties and the agreement of characters. $\square$

**Remark 1.9.8 (Formalization).** In [DefiniteBesselPeriodSesquilinear.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DefiniteBesselPeriodSesquilinear.lean#L347) the form $b$ is $0$ when no volume pair, unit pair or section exists, and the identity is then vacuous. The independence of choices is `perF_indep` at line 291, and the finiteness fact is `exchangeFinite` at line 274. The Bessel datum is defined in [BesselDatum.lean](lean:Development/AbelianVarietyTheory/BlockTheory/HeightDefect/BesselDatum.lean#L16). In [ExistsRealisedE.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsRealisedE.lean#L270) the Bessel normalising constant is $1$ and the lifts are $0$ off the admissible pairs. The input theorem of realisation is `exists_allTied_eqTied_on_of_realised` ([ExistsAllTiedEqTiedOnOfRealised.lean](lean:Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsAllTiedEqTiedOnOfRealised.lean#L28)); I did not unfold it, and the last proof names only its inputs.
