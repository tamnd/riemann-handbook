---
title: Local components and constant term systems
decls:
  - UpperTheory.ConvolutionTheory.Dp.locIff
  - UpperTheory.ConvolutionTheory.BW.exists_sys
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local components and constant term systems

This section collects two spectral inputs of the trace comparison below the step [EveryCharacter](/step/every-character/). The first reads the local component of a cuspidal representation inside its $L^2$ realisation. The second puts the operators that act on iterated constant terms of an automorphic form into one commutative algebra, so that the constant terms become a module over a polynomial ring in shifts, derivatives and central elements. Both are stated over a totally complex field. The next section uses the same spectral setting for a bound on Hecke operators.

### Local components in an $L^2$ summand

Let $E$ be a totally complex number field and $n \ge 1$. Let $\mathrm{GL}_n^1(\mathbb{A}_E)$ be the group of adelic matrices whose determinant has idele norm $1$, let $\mu$ be a Haar measure on it, and let $L^2(\mu)$ be the space of square integrable functions on $\mathrm{GL}_n(E) \backslash \mathrm{GL}_n^1(\mathbb{A}_E)$ for the quotient measure. The group acts on $L^2(\mu)$ by right translation, and this action is unitary.

**Definition 7.21.1 (Summand carrying a representation).** A summand is a nonzero closed subspace $V$ of the cuspidal part of $L^2(\mu)$ that is stable under right translation and has no closed stable subspace other than $0$ and $V$. Let $\pi$ be a cuspidal automorphic representation of $\mathrm{GL}_n(\mathbb{A}_E)$, realised as a space of cusp forms. The summand $V$ carries $\pi$ if the cusp forms of $\pi$ are exactly the central cusp forms whose class in $L^2(\mu)$ lies in $V$.

For a finite place $w$ of $E$ the group $\mathrm{GL}_n(E_w)$ acts on $L^2(\mu)$ by right translation, through its embedding into $\mathrm{GL}_n(\mathbb{A}_E)$ followed by the retraction onto $\mathrm{GL}_n^1(\mathbb{A}_E)$. A summand is stable under this action; we write $\lambda_w$ for the restricted action on $V$. A smooth irreducible representation $\sigma$ of $\mathrm{GL}_n(E_w)$ is a local component of $\pi$ at $w$ if there is a nonzero linear map from $\sigma$ to the space of $\pi$ that intertwines $\sigma$ with the action of $\mathrm{GL}_n(E_w)$ on $\pi$.

**Theorem 7.21.2 (Local components in an $L^2$ summand).** Let $E$ be totally complex, $\pi$ a cuspidal representation of $\mathrm{GL}_n(\mathbb{A}_E)$, $\mu$ a Haar measure on $\mathrm{GL}_n^1(\mathbb{A}_E)$ and $V \subset L^2(\mu)$ a summand that carries $\pi$. Let $w$ be a finite place and $\sigma$ a smooth irreducible representation of $\mathrm{GL}_n(E_w)$. Then $\sigma$ is a local component of $\pi$ at $w$ if and only if there is a nonzero linear map $f \colon \sigma \to V$ with
$$f(\sigma(g)x) = \lambda_w(g)f(x) \quad (g \in \mathrm{GL}_n(E_w)).$$

Lean: `UpperTheory.ConvolutionTheory.Dp.locIff`.

We use two facts. (a) There is an injective linear map $J$ from the space of $\pi$ to $V$, with dense image, that intertwines the action of $\mathrm{GL}_n(E_w)$ on $\pi$ with $\lambda_w$. (b) The representation $\pi$ has an adelic decomposition with local factors $\pi_w$, which are smooth, irreducible and admissible, and $\sigma$ is a local component of $\pi$ at $w$ if and only if $\sigma \cong \pi_w$. In particular there is a nonzero intertwiner $j \colon \pi_w \to \pi$.

*Proof.* If $\sigma$ is a local component, take a nonzero intertwiner $\sigma \to \pi$ and compose it with $J$. The composite is nonzero because $J$ is injective, and it intertwines by (a).

Conversely let $f \colon \sigma \to V$ be nonzero and equivariant. Put $i = J \circ j \colon \pi_w \to V$. For an adelic $a$ with component $1$ at $w$, right translation $R(a)$ commutes with the action of $\mathrm{GL}_n(E_w)$. We claim that there are such an $a$, a vector $y$ of $\pi_w$ and a vector $x$ of $\sigma$ with $\langle R(a)i(y), f(x)\rangle \ne 0$. If not, let $S$ be the span of all $R(a)i(y)$ with $a_w = 1$. The subspace $V \cap S^\perp$ is closed. It is stable under right translation: for $g$ in $\mathrm{GL}_n^1(\mathbb{A}_E)$, write $g^{-1}a$ as a product of its part away from $w$ and its part at $w$, and use that $i$ intertwines at $w$ and $R$ is unitary. By irreducibility, $V \cap S^\perp$ is $0$ or $V$. It contains every $f(x)$, and $f \ne 0$, so it is $V$. Then it contains $i(y)$ for every $y$, and $\langle i(y), i(y)\rangle = 0$ gives $i = 0$, which is false since $j \ne 0$ and $J$ is injective. This proves the claim.

Replace $f$ by $R(a)^{-1} \circ f$, which is still equivariant at $w$ and pairs nonzero with $i(y)$. Now we use a projection lemma: let $\rho$ be a unitary representation on a Hilbert space, $\sigma$ a smooth representation, $\tau$ an admissible representation, $i \colon \tau \to \rho$ and $f \colon \sigma \to \rho$ intertwiners with $\langle i(y_0), f(x_0) \rangle \ne 0$ for some $x_0, y_0$. Then there is a nonzero intertwiner $f' \colon \sigma \to \rho$ with values in the image of $i$. Its proof projects $f$ orthogonally onto the closure of the image of $i$; since a vector of $\sigma$ is fixed by a compact open subgroup and $\tau$ has finite-dimensional spaces of fixed vectors, the projected vectors lie in the image of $i$ itself. Apply it with $\tau = \pi_w$. Since $J$ is injective, $f'$ factors through a nonzero equivariant map $\sigma \to \pi$. So $\sigma$ is a local component. $\square$

### Constant term systems

Let $S$ be a set of places of $E$, containing the archimedean ones. We use the following objects; their definitions are recalled only as far as the statement needs them.

**Definition 7.21.3 (Block and datum).** A block of size $r$ off $S$ is a nonzero cusp form $f$ on $\mathrm{GL}_r(\mathbb{A}_E)$, invariant under a fixed central section, lying in a summand of $L^2$, with an infinitesimal character $\Lambda = (\Lambda_{\tau,i})$ indexed by the complex embeddings $\tau$ of $E$ and $1 \le i \le r$, and with Satake parameters at every finite place outside $S$. A datum of size $n$ is a finite list $d = (f_1, \dots, f_\ell)$ of blocks of sizes $r_1, \dots, r_\ell$ with $r_1 + \dots + r_\ell = n$. For $1 \le k \le n$ let $\iota(k)$ be the index of the block that contains position $k$, and put
$$\rho_j = \tfrac12\Big(\sum_{l < j} r_l - \sum_{l > j} r_l\Big).$$

For a smooth function $\varphi$ on $\mathrm{GL}_n(\mathbb{A}_E)$ the datum gives the iterated slice $c_d\varphi \colon \mathbb{R}^\ell \to \mathbb{C}$: take the constant term of $\varphi$ along the parabolic subgroup of type $(r_1, n - r_1)$, integrate it against the conjugate of $f_1$ over the norm-one quotient of $\mathrm{GL}_{r_1}$, repeat with the remaining blocks, and evaluate at the central exponents $t \in \mathbb{R}^\ell$.

For $C \ge 0$ let $B_C$ be the space of smooth functions on $\mathrm{GL}_n(\mathbb{A}_E)$ that are spherical at every finite place outside $S$ and satisfy uniform moderate growth bounds in which a central operator of degree $k$ costs a factor $C^k$. For a polynomial $P$ in the variables $z_{\tau,i}$ ($\tau$ an embedding, $1 \le i \le n$), let $z(P)$ be the corresponding element of the centre of the enveloping algebra acting on functions. For $w \notin S$ and $1 \le j \le n$ let $T_{w,j}$ be the Hecke operator of the double coset of $\mathrm{diag}(\varpi_w, \dots, \varpi_w, 1, \dots, 1)$ ($j$ entries $\varpi_w$), normalised by the factor $q_w^{-j(n-j)/2}$ and acting by right translation.

**Theorem 7.21.4 (Constant term system).** Let $E$ be totally complex, $d$ a datum of size $n$ off $S$ with $\ell$ blocks, and $C \ge 0$. There are a commutative $\mathbb{C}$-algebra $A$ acting on $B_C$, elements $Z_{\tau,i}$, $H_{w,j}$, $I_1, \dots, I_\ell$ of $A$ and a homomorphism $v \mapsto t(v)$ from $(\mathbb{R}^\ell, +)$ to the multiplicative monoid of $A$, such that:

1. for every polynomial $P$, $P(Z)$ acts on $B_C$ as $z(P)$;
2. for $w \notin S$, $H_{w,j}$ acts on $B_C$ as $T_{w,j+1}$;
3. the map $\iota$ is surjective;
4. $c_d(t(v)\varphi)(x) = c_d\varphi(x + v)$ for all $v, x \in \mathbb{R}^\ell$;
5. $c_d(I_j\varphi)$ is the derivative of $c_d\varphi$ in the direction $e_j$;
6. $c_d(Z_p\varphi) = c_d(E_p(\Lambda + I_\iota)\varphi)$, where $E_p$ is a polynomial attached to $p = (\tau, i)$ and $\Lambda + I_\iota$ is the family $\Lambda_{\tau,k} + I_{\iota(k)}$;
7. for $w \notin S$, $c_d(H_{w,j}\varphi) = c_d(h_{w,j}(I, t)\varphi)$, where $h_{w,j}$ is the Satake polynomial of the blocks at $w$, with the parameters of block $j$ shifted by $q_w^{-\rho_j}$, evaluated at the shifts $t$ and the derivatives $I$;
8. for each $\varphi$, $\beta$ and $R$ there is $B$ with $|c_d(Z^\alpha I^\beta\varphi)(x)| \le BC^{|\alpha|}$ for all monomials $Z^\alpha$ and all $|x| \le R$.

Lean: `UpperTheory.ConvolutionTheory.BW.exists_sys`.

*Proof.* Consider the set of operators on $B_C$ made of the central operators, the derivatives $I_j$ in the central exponents of the blocks, the right translations by the central elements $t(v)$ of the Levi subgroup, and the Hecke operators $T_{w,j}$ for $w \notin S$. Each maps $B_C$ to itself, and they commute pairwise. The derivatives $I_j$ are given by elements of the enveloping algebra, and the $t(v)$ are right translations by archimedean elements. Central elements commute with the enveloping algebra and with archimedean right translations, Hecke operators at finite places commute with both, and $t(v)t(v') = t(v + v')$. A commuting family of endomorphisms of a vector space lies in a commutative subalgebra of the endomorphism ring; let $A$ be this algebra. Statements 1 and 2 then hold by construction. The basic properties of data give the rest: $\iota$ is surjective, the infinitesimal characters of a block sum to $0$, the translation $v \mapsto t(v)$ is additive with $t(0) = 1$, the slice of a translate is the shifted slice, and the slices of central and Hecke operators are as in 6 and 7. The growth bound 8 comes from the definition of $B_C$. $\square$

The system is used in a vanishing argument: when one entry of $\Lambda$ is larger than a bound that depends only on $C$ and on the block sums of $\Lambda + \rho$, the slice $c_d$ vanishes on $B_C$.

**Remark 7.21.5 (Formalization).** The local component theorem is [LocIff.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/LocIff.lean#L55), with the statement at [LocalRepresentationL2.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/CentreSplitting/LocalRepresentationL2.lean#L142); fact (a) is `locEmb`, fact (b) is `locFlath` with `nonempty_adelicDecomposition`, and the projection lemma is the private `proj_range` (line 13). We did not unfold the retraction `retractOne` onto the norm-one group, nor `locComp`, beyond its use as the existence of a nonzero intertwiner. The constant term system is at [CommuteCenterRtInfGL.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/CommuteCenterRtInfGL.lean#L176); the algebra comes from `exists_alg` and the private `ops_comm`, and properties 3 to 8 are the fields of `AbsSys` in [SliceShift.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/BlockHeckeSlices/SliceShift.lean#L13), fed by `datBasics`. We did not unfold `blockE`, `hEP`, `lift` or `Band`, so the descriptions of $E_p$, $h_{w,j}$ and $B_C$ above are only as precise as the statement requires.
