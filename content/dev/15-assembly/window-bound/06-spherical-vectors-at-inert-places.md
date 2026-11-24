---
title: Spherical vectors at inert places
decls:
  - PositivityTheory.Sph.howeInert
  - PositivityTheory.Sph.locDataV
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Spherical vectors at inert places

This section proves a local fact on the [[Weil representation|H3Q2703KKV]] of a unitary dual pair at a place of $F$ that is inert in $E$. At such a place the vacuum vector is fixed by the integral points of both [[unitary groups|0R9R0Y1HDK]], and the vectors fixed by the integral points of one group are spanned by the translates of the vacuum under the other group. The result feeds the spherical part of Howe duality at the unramified places, which [Theorem 2.6.4 of Volume 12](/entry/theorem-k-head2-of-mod/) uses, and through it the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). The Weil representation and its lattice model are in [the Weil representation](/learn/theta/#the-weil-representation).

We fix the data of the theta lifts of Volume 12. Let $E/F$ be a CM extension with conjugation $\sigma$, with $E/\mathbb{Q}$ Galois and $E/F$ unramified at all finite places. Let $\psi$ be a standard additive character of $\mathbb{A}_F$. Let $V$ and $V'$ be Hermitian spaces over $E$ of dimensions $a$ and $a'$, and let $W$ be a skew-Hermitian space of dimension $a + a'$, each with a fixed lattice. Let $\omega$ be the Weil representation of $U(V) \times U(W)$ on the [[Schwartz space|GE020MY43M]] of $M_{a \times (a+a')}(\mathbb{A}_E)$, with the characters $\alpha$ and $\beta$, and let $\omega'$ be the one of $U(V') \times U(W)$. The characters $\alpha$ and $\beta$ are unramified outside a finite set $T$ of places of $F$, and each place of $T$ splits in $E$. We call all this a *good triple*. Its conditions also say: at each place $v$ of $F$ that is inert in $E$, the residue characteristic is odd, the norm of $v$ is larger than $3$, and $\psi_v$ has conductor $\mathcal{O}_{F_v}$.

Fix a finite place $v$ of $F$. For a Hermitian or skew-Hermitian space $Y$ in the triple, let $U(Y)_v$ be the elements of $U(Y)(\mathbb{A}_F)$ that are trivial away from $v$, and let $K_Y \subseteq U(Y)_v$ be the stabilizer of the lattice of $Y$ at $v$. The local Weil representation at $v$ is a pair $(\omega_v, \rho_v)$: $\omega_v$ is an action of $U(V)_v \times U(W)_v$ and $\rho_v$ an action of the Heisenberg translations at $v$, on the Schwartz space $\mathcal{S}_v$ of $M_{a \times (a+a')}(F_v \otimes E)$, both compatible with the global actions. Let $\varphi_v^0 \in \mathcal{S}_v$ be the vacuum vector of the model.

**Definition 2.6.1 (Howe property).** The local Weil representation $(\omega_v, \rho_v)$ has the *Howe property* at $v$ if:

1. $\omega_v(g, 1)\varphi_v^0 = \varphi_v^0$ for each $g \in K_V$, and $\omega_v(1, k)\varphi_v^0 = \varphi_v^0$ for each $k \in K_W$;
2. each $\varphi \in \mathcal{S}_v$ fixed by $\omega_v(K_V \times 1)$ lies in the span of the vectors $\omega_v(1, h)\varphi_v^0$ with $h \in U(W)_v$;
3. each $\varphi \in \mathcal{S}_v$ fixed by $\omega_v(1 \times K_W)$ lies in the span of the vectors $\omega_v(g, 1)\varphi_v^0$ with $g \in U(V)_v$.

Lean: `PositivityTheory.Sph.IsHowe`.

Part 2 says that the $K_V$-spherical vectors are reached from the vacuum by $U(W)_v$ alone. This is the form of Howe duality that the spherical theta lift needs: the $K_V$-fixed part of $\mathcal{S}_v$ is a cyclic module over $U(W)_v$.

**Definition 2.6.2 (Local data at $v$).** Let $w$ be the place of $E$ above $v$, and $L = E_w$. *Local data* for $(V, W)$ at $v$ consist of a uniformizer $\varpi$ of $L$, the conjugation $\sigma_L$ of $L$ over $F_v$, an odd number $q$ such that the residue field of $L$ has $q^2$ elements, $\sigma_L$ fixes $\varpi$, and $\sigma_L$ acts nontrivially on the residue field, a unit $\delta \in L$ with $\sigma_L(\delta) = -\delta$, integral Hermitian matrices $J_S \in GL_a(\mathcal{O}_L)$ and $J_T \in GL_{a+a'}(\mathcal{O}_L)$, a character $\psi_L$ of $L$, a vector $s \in \mathcal{S}_v$, operators $\rho_L(x)$ for $x \in M_{(a+a') \times a}(L)$ and a representation $\omega_L$ of $U(J_S) \times U(J_T)$ on $\mathcal{S}_v$, and maps $\iota_S : U(J_S) \to U(V)_v$ and $\iota_T : U(J_T) \to U(W)_v$, with the following properties:

1. $\psi_L$ is trivial on the integers of $L$ fixed by $\sigma_L$, and is not trivial on $\varpi^{-1}\mathcal{O}_L^{\sigma_L = 1}$;
2. $\rho_L(0) = 1$ and $\rho_L(x)\rho_L(y) = \psi_L\big(\tfrac12(H(x,y) + \sigma_L H(x,y))\big)\rho_L(x+y)$, with $H(x, y) = \delta\,\mathrm{tr}(J_S^{-1}\,{}^t\bar y\,J_T\,x)$;
3. $\omega_L(g, h)\rho_L(x) = \rho_L(h x g^{-1})\,\omega_L(g, h)$;
4. $s \neq 0$, $s = \varphi_v^0$, $\rho_L(u)s = s$ for each integral $u$, and the vectors $\rho_L(x)s$ span $\mathcal{S}_v$;
5. if $g$ and $h$ are integral, then $\omega_L(g, h)$ fixes each vector fixed by all $\rho_L(u)$ with $u$ integral;
6. $\iota_S$ and $\iota_T$ send integral points into $K_V$ and $K_W$, and $\omega_L(g, h)$ is the action of $(\iota_S(g), \iota_T(h))$ under the global Weil representation.

Lean: `PositivityTheory.Sph.LocData` (also `GlobalTheory.Hk3.LocPair`).

The local data are a lattice model of the local Weil representation of the unramified dual pair $(U(J_S), U(J_T))$. Properties 1 to 5 refer only to $L$; property 6 ties the model to the global one.

**Lemma 2.6.3 (Local data at an inert place).** Let the triple be good, let $v$ be a place of $F$ inert in $E$, with $w$ above $v$, and let $v \notin T$. Then local data for $(V, W)$ at $v$ exist.

Lean: `PositivityTheory.Sph.locDataV`.

*Proof.* We use seven local facts, each a theorem of the formalization that we read by its statement.

1. The completion $L = E_w$ has a uniformizer $\varpi$, an odd $q$, a unit $\delta$ with $\sigma_L(\delta) = -\delta$, and a character $\psi_L$ with property 1, together with an embedding $\iota$ of $L$ into $\mathbb{A}_E$ onto the elements supported at $v$, with $\psi(\mathrm{tr}\,\iota(x)) = \psi_L(x + \sigma_L x)$.
2. The lattices of $V$ and $W$ at $v$ have unimodular Hermitian frames $J_S$ and $J_T$, with coordinates that identify the lattice of $M_{a \times (a+a')}$ at $v$ with the integral matrices, and give $\iota_S$ and $\iota_T$ with property 6 for $K$.
3. A Schrödinger family $\rho_L$ with property 2 exists, and the vectors $\rho_L(x)s$ span $\mathcal{S}_v$ for each $s \neq 0$.
4. Local Weil operators $\omega_L$ exist that agree with the global action.
5. The operators $\omega_L$ normalize $\rho_L$ as in property 3.
6. The vacuum $\varphi_v^0$ is fixed by $\rho_L(u)$ for each integral $u$, and each vector with this property is a multiple of $\varphi_v^0$.
7. For $k \in K_V$ and $k' \in K_W$, the global Weil representation fixes $\varphi_v^0$ under $(k, k')$.

Put $s = \varphi_v^0$. It is nonzero, so facts 3 and 6 give property 4. For property 5, let $g$ and $h$ be integral, and let $s'$ be fixed by all $\rho_L(u)$ with $u$ integral. By fact 6, $s' = c\,s$ for some $c \in \mathbb{C}$. By facts 2 and 7, $\iota_S(g) \in K_V$ and $\iota_T(h) \in K_W$ fix $s$, so by fact 4 the operator $\omega_L(g, h)$ fixes $s$, and so it fixes $s'$. The other properties are facts 1 to 5. $\square$

The central input is a local theorem of Howe on the unramified dual pair.

**Theorem 2.6.4 (Unramified Howe duality).** Let $L$ be a complete discretely valued field of characteristic $0$, with local data $(\varpi, \sigma_L, q, \delta, J_S, J_T, \psi_L, \rho_L, \omega_L)$ satisfying properties 1 to 5. Let $s \neq 0$ be fixed by all $\rho_L(u)$ with $u$ integral, with the vectors $\rho_L(x)s$ spanning the space. Then each vector fixed by $\omega_L(g, 1)$ for all integral $g \in U(J_S)$ lies in the span of the vectors $\omega_L(1, h)s$, and the same holds with the roles of $J_S$ and $J_T$ exchanged.

Lean: `GlobalTheory.Hk3.howeUnram_holds`.

*Proof.* This is Howe's theorem on the spherical vectors of an unramified dual pair [Howe 1979]. The formalization proves the first half directly and gets the second half by exchanging $J_S$ and $J_T$ through the Hermitian adjoint. We do not reproduce its proof here. $\square$

**Theorem 2.6.5 (Howe property at inert places).** Let the triple be good, and let $v$ be a finite place of $F$ such that there is no $F$-embedding $E \to F_v$. Then each local Weil representation $(\omega_v, \rho_v)$ of $(V, W)$ at $v$ has the Howe property, and so has each local Weil representation of $(V', W)$ at $v$.

Lean: `PositivityTheory.Sph.howeInert`.

*Proof.* Since $E \otimes_F F_v$ is a field and $E/F$ is unramified, $v$ is inert in $E$; let $w$ be the place above it. Each place of $T$ splits in $E$, so $v \notin T$. Hence $\alpha$ and $\beta$ are unramified at each place of $E$ above $v$, and so is $\beta/\alpha$.

Consider $(V, W)$. The Weil representation is attached to the characters $\beta$ on $V$ and $\beta/\alpha$ on $W$. Since both are unramified above $v$, the global vacuum is fixed by $K_V$ and by $K_W$; with the compatibility of $\omega_v$ and the global action, this is part 1. By the lemma, local data for $(V, W)$ at $v$ exist. Apply the theorem on unramified Howe duality to them, with $s = \varphi_v^0$. A vector $\varphi$ fixed by $\omega_v(K_V \times 1)$ is fixed by $\omega_L(g, 1)$ for each integral $g$, by property 6. So it lies in the span of the $\omega_L(1, h)s = \omega_v(1, \iota_T(h))\varphi_v^0$, which is part 2. Part 3 is the same with the roles exchanged.

For $(V', W)$ the argument is the same, with $\alpha$ and $\beta$ exchanged and with the local data for $(V', W)$ at $v$. $\square$

**Remark 2.6.6 (Formalization).** The hypothesis of `howeInert` is `IsEmpty (E →ₐ[F] Fv F v)`, and the step to "inert" is `inert_ctx` ([UnrAtDiv.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/UnrAtDiv.lean#L13)). The two vacuum statements are `fix_of` in the same file. The definition of the Howe property is `IsHowe` ([HoweInert.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/HoweInert.lean#L26)), and `howeInert` proves the statement `HoweInert` of line 60. It is used only through `vacInert`, which gives the spherical statement `VacInert`. The local data `LocData` are in [HoweDefs.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/HoweDefs.lean#L14), and the local Howe theorem is `howeUnram_holds` ([RhoMemOfMkEq.lean](lean:Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L250)), applied in `gen_of`. Odd points:

- The seven local facts of the lemma are theorems in `GlobalTheory.T` whose proofs are each one line, `first | exact @X | exact X | (intros; apply X <;> assumption)`, for a theorem `X` of another namespace, under `maxHeartbeats 1000000`; for example [InertPlaceLatticeVacuumFixedAndUniqueStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/InertPlaceLatticeVacuumFixedAndUniqueStatement.lean#L21). We read their statements only.
- The local data for $(V', W)$ come from a second lemma, `locDataV'` ([LocDataVAlt.lean](lean:Development/WeilBound/ThetaLifts/SphericalLattices/LocDataVAlt.lean#L21)), which uses a different chain of nine local facts and takes $L$ to be the completion of $E$ at $w$; `locDataV` takes $L$ from fact 1. The two proofs build the same kind of object in two ways.
- The file HoweInert.lean also defines `SphFun`, `IrrAt` and `SphSplit`, which `howeInert` does not use.
