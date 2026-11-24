---
title: Approximate Lagrangian projections for pairs of lattices
decls:
  - PI.SqPairLocal.sqPairLocal_of
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Approximate Lagrangian projections for pairs of lattices

The bounds for orbital integrals compare two unimodular Hermitian lattices $L'$ and $L''$ of even rank. They need one matrix $e$ that preserves both lattices and that is, at a given prime $p$ and up to a given modulus $n$, the projection onto a Lagrangian subspace along a complementary Lagrangian subspace. This section proves that such a matrix exists. The local input is a Cartan decomposition for unitary similitudes over an unramified quadratic extension of a local field. The result is the theorem on [square pairs](/entry/square-pair-local/) of the chapter on orbital bounds.

### Lattices over a CM field

Let $E$ be a number field with an involution $x \mapsto \bar x$ and ring of integers $\mathcal{O}_E$ (see [number fields](/learn/number-fields/#number-fields-and-their-integers)). On $E^N$ let $h(x, y) = \sum_i \bar x_i y_i$ be the standard Hermitian form, and write $A^* = \bar A^{\mathsf T}$ for a matrix $A$, so that $h(Ax, y) = h(x, A^* y)$.

**Definition 7.2.1 (CM field unramified at all finite places).** The field $E$ with its involution is *CM and unramified* if $E$ is totally complex, every embedding $\varphi : E \to \mathbb{C}$ satisfies $\varphi(\bar a) = \overline{\varphi(a)}$, and for every maximal ideal $P$ of $\mathcal{O}_E$ there is $\theta \in \mathcal{O}_E$ with $\theta - \bar\theta \notin P$.

The last condition says that the different of $E$ over its fixed field is prime to every $P$: the quadratic extension is unramified at each finite place.

**Definition 7.2.2 (Self-dual lattice).** A subset $L \subseteq E^N$ is a *self-dual lattice* if it is a finitely generated $\mathcal{O}_E$-submodule that spans $E^N$ over $E$, and $y \in L$ if and only if $h(x, y) \in \mathcal{O}_E$ for all $x \in L$.

So $L$ is its own dual for $h$: it is a unimodular Hermitian lattice in the sense of [lattices in Hermitian spaces](/learn/hermitian-lattices/#lattices-in-quadratic-and-hermitian-spaces).

### The local Cartan pair

We take the following local statement as given. It is proved elsewhere in the development, and the [theorem](/entry/square-pair-local/) that uses the result of this section supplies it.

**Theorem 7.2.3 (Local Cartan pair).** Let $R$ be a commutative ring with an involutive automorphism $\sigma$. Assume that the fixed ring $R_0 = \{x : \sigma x = x\}$ is a Henselian discrete valuation ring with finite residue field, and that $\theta - \sigma\theta$ is a unit of $R$ for some $\theta \in R$. Let $\varpi$ be an irreducible element of $R_0$, let $N$ be even, $k \geq 0$, and let $h \in M_N(R)$ satisfy $\sigma(h)^{\mathsf T} h = \varpi^{2k} \cdot 1$. Then there are $e, f \in M_N(R)$ with
$$e^2 = e, \qquad \sigma(e)^{\mathsf T} = 1 - e, \qquad e h = h f.$$

The two conditions on $e$ say that $e$ is the projection onto a Lagrangian submodule $\operatorname{im} e$ along the Lagrangian submodule $\ker e$: indeed $\sigma(e)^{\mathsf T} e = (1 - e) e = 0$, so $\operatorname{im} e$ is isotropic, and the same holds for $1 - e$. The ring $R$ plays the part of the ring of integers of the unramified quadratic extension of a nonarchimedean local field, and $h$ is a similitude of the standard form with factor $\varpi^{2k}$. The statement is a form of the Cartan decomposition of the unitary group over an unramified extension: a similitude moves the standard Lagrangian decomposition into a decomposition of the same kind.

### The global statement

**Theorem 7.2.4 (Square pairs at a prime).** Assume the local Cartan pair theorem. Let $E$ be CM and unramified, let $N$ be even, let $L'$ and $L''$ be self-dual lattices in $E^N$, let $n \in \mathcal{O}_E$ be nonzero and let $p$ be a prime number. Then there is $e \in M_N(E)$ with $e L' \subseteq L'$ and $e L'' \subseteq L''$ such that for every
$$M \in \{\, e^2 - e,\ e^* e,\ (1 - e)^*(1 - e) \,\}$$
and every $y \in L' \cup L''$ there are $s \in \mathbb{Z}$ with $p \nmid s$ and $m \in L' \cap L''$ with $s \cdot M y = n \cdot m$.

Lean: `PI.SqPairLocal.sqPairLocal_of`.

So $e$ is a Lagrangian projection modulo $n$, after inverting the integers prime to $p$.

*Proof.* There are four steps.

First, an integer multiple of each lattice lies in the other. There is a nonzero $c \in \mathbb{N}$ with $c\, y \in n (L' \cap L'')$ for all $y \in L' \cup L''$, since $L'$, $L''$ and $n(L' \cap L'')$ are lattices in the same space. Write $c = p^a c'$ with $p \nmid c'$.

Second, the problem is reduced to the primes $Q$ of $\mathcal{O}_E$ above $p$. Call $e$ *good at $Q$ for the constant $p^a$* if $e^2 - e$ and $e + e^* - 1$ map $L'$ and $L''$ into $p^a L'$ and $p^a L''$ after multiplication by some $s \notin Q$. The identities
$$\begin{aligned} e^* e &= -(e^2 - e) + (e + e^* - 1) e, \\ (1 - e)^*(1 - e) &= -(e^2 - e) - (e + e^* - 1)(1 - e) \end{aligned}$$
show that the three matrices $M$ are then small at $Q$ too, because $e$ and $1 - e$ preserve both lattices. Given a good $e$ at all $Q \mid p$, for $y \in L' \cup L''$ and each $Q \mid p$ we get $s \notin Q$ and $m$ in $L'$ or $L''$ with $s M y = p^a m$, and then $c' \cdot s M y = s' n m'$ with $m' \in L' \cap L''$ by the first step. A local-global principle for modules over $\mathcal{O}_E$ (an element that lies in a submodule after multiplication by some $s \notin Q$ for each $Q \mid p$ lies in it after multiplication by an integer prime to $p$) gives the integer $s$ of the theorem.

Third, the good matrices at the single primes are glued. By the Chinese remainder theorem in $\mathcal{O}_E$, and since a high power of $Q$ is divisible by a given nonzero $c$ up to a unit at $Q$, it is enough to find, for each maximal $Q$ and each nonzero constant, a matrix $e$ that preserves both lattices and is good at $Q$ and at $\bar Q$. If $\bar Q \neq Q$, so that $Q$ splits, this is a direct construction at a split place.

Fourth, let $\bar Q = Q$, so that $Q$ is inert. The completion of $\mathcal{O}_E$ at $Q$, with the involution, is a ring $R$ as in the local Cartan pair theorem, and $\mathcal{O}_E$ is dense in it. A self-dual lattice is, locally at $Q$, the image of the standard lattice under a unitary matrix $G$. The unitary matrix $u$ that relates the local frames of $L'$ and $L''$ satisfies $u^* u = 1$, so $\varpi^k u$ satisfies the hypothesis of the local Cartan pair theorem for $k$ large enough that it is integral. The theorem gives an exact Lagrangian projection $e$ in the completion that is adapted to both lattices. Approximate $e$ by a matrix over $E$ to a high power of $\varpi$. The approximation is good at $Q$. $\square$

**Remark 7.2.5 (Formalization).** The local Cartan pair theorem is a hypothesis of the statement here; its caller supplies it. The goodness condition in the proof is stated with $e + e^* - 1$, not with $e^* - (1 - e)$, which is the same matrix. The existence of the completion, the local description of self-dual lattices, the approximation step and the construction at split places are proved lemmas that we did not unfold; the outline above follows their statements. The theorem is in [SqPairLocalOf.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/SquarePairLocal/SqPairLocalOf.lean#L18), and the reduction steps are in [SqPairLocalOfSteps.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/SquarePairLocal/SqPairLocalOfSteps.lean#L265).
